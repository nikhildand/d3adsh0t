# 🔶 d3adsh0t !! 🔶


![](/samples/d3adsh0t.png)


** Neural Object Detection for First-Person-Shooting Games in Python **

## Disclaimer :

**'d3dsh0t' is a Neural Object Detection for Allies and Enemies in FPS Games, It is purely experimental and is intended only for educational purposes.**

Since this repo is open source, its just one google search away from cheaters abusing it, and I am not a fan of cheating in 'online multiplayer games', so I wont be uploading 'my' weights for the model.

If you truly believe in learning new stuff and would like to try out this repo, you should be able to build your own Data-Set and should be able to train a YOLOv5s model, this repo is solely aimed at those people who believe in learning and put out an effort.

## Prerequisites :

I would suggest you to setup a virtual environment and clone the repo from version control, its left to your discretion though.

**-> Major Requirements :**

1) Windows 10 64 bit and NVIDIA graphics card
2) CUDA Installation : https://developer.nvidia.com/cuda-10.2-download-archive
3) Python >= 3.6
3) Cython
4) Numpy >= 1.18.5
5) Opencv-python
6) Torch >= 1.5.1, Torchvision >= 0.6 (Installation is a bit different for this, refer : https://pytorch.org/get-started/locally/) 
7) PyYAML >= 5.3
8) Pywin32


**-> Minor Requirements :** (If imports are optimized, you can omit these)

1) Scipy
2) Tqdm
3) Matplotlib
4) Pillow


**-> Optional** : (If you decide to change the way you manage mouse_events and mouse movements) 

1) Interception Driver : https://www.oblita.com/interception.html (It is Digitally Signed) [Install with 'cmd' as Administrator]

```
Original Author's GitHub : https://github.com/oblitum/Interception [C++], 
Python Wrapper by 'dc740': https://github.com/dc740/AutoHotPy

NOTE : Managing' Mouse-Inputs' depends on the game, normally games patch many mouse_events and movements,
So I resorted to this driver, if you dont know what you are doing when using this driver I highly recommend
you not to use it, because if not coded properly in rare cases you could damage your PC, and I am not responsible
for any damage done to your computer, although if you dont tweak my code w.r.t that driver in 'd3adsh0t.py'
you should be fine.
```

## Yolov5s :

This project utilizes the **Yolov5s** architecture : https://github.com/ultralytics/yolov5 (Credits to Ultralytics for providing the base code for the YOLO architecture)

## Performance And Inference :

**Note:** The FPS discussed is only **Processing FPS** your **in-game gameplay FPS wont be affected**.

**'d3adsh0t'** in game is able to **Process Detections** at around 35 - 40 frames per seconds, this drops to around 25 - 28 (**In python world 'it is fast'**) frames per second when the Main-Thread waits for Cursor Movement when an enemy is detected on a **Overclocked GTX 1080Ti** and **Intel Core i9-9900K**, so it anyways wouldn't give any significant advantage, it is just a proof of concept.

## How To Use ?!!

1) Prepare your Data-Set. (Different Angle, Different Exposure, Different Distance's)

1) Train an agent. (Invest most of your time here, your models performance depends on this)

2) Run any FPS game. (In my case, it was Valorant) in 'Windowed Mode'

3) Change the **'region=()'** parameter of grab_screen(**''**) in d3adsh0t.py to your convenience, if you dont pass anything, it will take the whole screen, processing (grab_screen and other stuff) such input is way too time taking and not worth it, **I would suggest a resolution to 1280x720** or even less for better performance.

4) Run **'d3adsh0t.py'** and start a game.

## 'd3adsh0t' In Action :

### 'd3adsh0t' identifying Allies

![](/samples/example_1_d3adsh0t.gif)

### 'd3adsh0t' differentiating Allies and Enemies

![](/samples/example_2_d3adsh0t.gif)
