from grabscreen import grab_screen
from interception.AutoHotPy import *
from models.experimental import *
from utils.datasets import *
import threading
import win32api
import argparse

d3adsh0t = None
MovingCursor = False


def MouseManagingThread():
    """
    This function runs through a thread, which intercepts mouse inputs before being passed to hardware for processing,
    and changes position of cursor to the predicted location of 'Enemy' from the Neural Net when an enemy is detected.

    (Main thread continues after cursor has been moved to the d3adsh0t coordinate, is thread safe)

    (The cursor position is given by the helper function "target_d3adsh0t")
    """

    global d3adsh0t, MovingCursor

    def exitAutoHotKey(autohotpy, event):
        autohotpy.stop()

    def MoveCursorPosition(autohotpy, event):
        if not ShotTarget.is_set() and (d3adsh0t is not None):
            print('Moving')
            autohotpy.moveMouseToPosition(d3adsh0t[0], d3adsh0t[1])
            MovingCursor = True
            ShotTarget.set()
            MovingCursor = False
        else:
            MovingCursor = False

    MouseManager = AutoHotPy()
    MouseManager.registerExit(MouseManager.ESC, exitAutoHotKey)
    MouseManager.registerForKeyHold(MouseManager.LEFT_ALT, MoveCursorPosition)
    MouseManager.start()


def ShootTargetThread():
    """
    This function also runs through a thread, is invoked when the cursor is moved to d3adsh0t.
    """

    # Keybd_event  : https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-keybd_event
    # Virtual Keys : https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

    while MovingCursor:
        win32api.keybd_event(0x01, 0x45, 0x0001 | 0, 0)  # Left Down

        '''Can add logic here for Recoil Control, check Anti-Recoil folder to log gunshots to get data 
        and use some basic statistics logics with regards to variance to control recoil, as Valorant induces
        some randomness in gun-recoil (although the pattern is almost the same)
        '''

        win32api.keybd_event(0x01, 0x45, 0x0001 | 0x0002, 0)  # Left Up


def target_d3adsh0t(BBOX, img):
    """
    This function stores the coordinate of d3adsh0t (Head - Chest Level) when a predicted enemy location's
    BBOX coor is given.
    """
    global d3adsh0t
    y_buffer = (BBOX[3] - BBOX[1]) // 10
    x1 = BBOX[0] + round((BBOX[2] - BBOX[0]) / 2)
    y1 = BBOX[1] + round((BBOX[3] - BBOX[1]) / 6) + y_buffer

    d3adsh0t = [x1, y1]

    # Debugging:
    # cv2.circle(img, (x1, y1), 2, (0, 0, 255), 2)


def detect():
    """
    Takes GameScreen as input, and is processed in YOLOv5 Object Detection Architecture, moves cursor through
    Interception driver, shoots enemy, resulting in ==> D3ADSH0T
    """
    weights, imgsz = \
        opt.weights, opt.img_size

    # -------------------------------------------------------------------------------------------------------------------
    # Initialize :

    device = torch_utils.select_device(opt.device)
    half = device.type != 'cpu'  # Half precision only supported on CUDA

    # -------------------------------------------------------------------------------------------------------------------
    # Load Model :

    model = attempt_load(weights, map_location=device)  # Load FP32 model
    imgsz = check_img_size(imgsz, s=model.stride.max())  # Check img_size
    if half:
        model.half()  # To FP16

    # -------------------------------------------------------------------------------------------------------------------
    # Get Names and Colors :

    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[0, 255, 0], [0, 0, 255]]  # (Ally, Enemy) = (Green, Red)

    # -------------------------------------------------------------------------------------------------------------------
    # Set DataLoader & Run D3ADSH0T :

    img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init Img
    _ = model(img.half() if half else img) if device.type != 'cpu' else None  # Run once

    print('\n Running d3adsh0t Aimbot...!!')

    while True:
        img = grab_screen()  # Make sure you mention the 'region=' parameter of GameScreen, else 'Whole Screen' will be taken.
        if img is not None:
            t1 = torch_utils.time_synchronized()
            im0 = img
            img = letterbox(img, new_shape=imgsz)[0]
            img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
            img = np.ascontiguousarray(img)
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # ---
            # Interface :
            pred = model(img, augment=opt.augment)[0]

            # ---
            # Apply NMS :
            pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes,
                                       agnostic=opt.agnostic_nms)

            if pred[0] is not None and len(pred[0]):
                target = \
                    [scale_coords(img.shape[2:], det[:, :4], im0.shape).round()[:, :4] for i, det in enumerate(pred) if
                     det[0, 5] == 1 and det is not None][0]
                target = [int(coor) for coor in torch.stack(sorted(target, key=lambda a: a[3] - a[1], reverse=True))[0]]
                target_d3adsh0t(target, im0)
                ShotTarget.clear()
                ShotTarget.wait()

            t2 = torch_utils.time_synchronized()
            print('FPS = (%.3fs)' % (1 / (t2 - t1)))

            # DeBugging Block: (Note: Comment out the above 'if' block before starting DeBugging for the below block)
            """# ---
            # Process detections:
            for i, det in enumerate(pred):
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Write results:
                    for *xyxy, conf, cls in det:
                        label = '%s %.2f' % (names[int(cls)], conf)
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)"""

            # DeBugging
            # cv2.imshow('Screen Projection', im0)
            # if cv2.waitKey(1) == ord('q'):  # q to quit
            #   raise StopIteration

    # ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='weights/Valorant_D3DSH0T.pt',
                        help='model.pt path(s)')
    parser.add_argument('--img-size', type=int, default=416, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.35, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    opt = parser.parse_args()

    MouseMoveThread = threading.Thread(target=MouseManagingThread)
    MouseClickThread = threading.Thread(target=ShootTargetThread)

    ShotTarget = threading.Event()
    ShotTarget.set()
    MouseMoveThread.start()
    #MouseClickThread.start()

    with torch.no_grad():
        detect()
