import pynput
import time
import random

# ----------------------------------------------------------------------------------------------------------------------
class ValorantAntiRecoil:
    """
    The Methods In This Class Manages Movements Of Mouse, Such That Recoil Is Reduced.
    """

    GunPatternDirectory = {
        'SPECTRE' : [(), (), (), (), (), (), (), (), ()],
        'VANDAL'  : [(), (), (), (), (), (), (), (), ()],
        'PHANTOM' : [(), (), (), (), (), (), (), (), ()],
        'BULLDOG' : [(), (), (), (), (), (), (), (), ()],
        'STINGER' : [(), (), (), (), (), (), (), (), ()]
    }

    def __init__(self, Sleep, Gun, MouseCoor):

        self.SleepTime = Sleep * 0.001
        self.Weapon = Gun
        self.InitMousePos = MouseCoor

    def ManageRecoil(self):

        for RelCoor in self.GunPatternDirectory[self.Weapon]:
            time.sleep(self.SleepTime)
            MouseController.move(RelCoor[0], RelCoor[1])

# ----------------------------------------------------------------------------------------------------------------------

def AntiRecoilData(Key):    # Keyboard-Thread
    """
    This Function Is Called Whenever A Key Is Clicked On Keyboard, Used As A Toggler.
    Usage : Toggle Anti-Recoil, Toggle Logger, Change Weapon
    """

    global AntiRecoilEnabled
    global Weapon
    global LoggingEnabled
    global RecoilPatternLog

    if Key == Toggler:
        AntiRecoilEnabled = not AntiRecoilEnabled
        if AntiRecoilEnabled:
            print('Anti-Recoil Enabled')

        else:
            print('Anti-Recoil Disabled')

    elif Key == pynput.keyboard.Key.f2:
        Weapon = 'SPECTRE'

    elif Key == pynput.keyboard.Key.f3:
        Weapon = 'VANDAL'

    elif Key == pynput.keyboard.Key.f4:
        Weapon = 'PHANTOM'

    elif Key == pynput.keyboard.Key.f5:
        Weapon = 'BULLDOG'

    elif Key == pynput.keyboard.Key.f6:
        Weapon = 'STINGER'

    if Key == pynput.keyboard.Key.f7:
        LoggingEnabled = not LoggingEnabled
        if LoggingEnabled:
            RecoilPatternLog = []
            print('Logging Values Enabled, (CLICK CAREFULLY AT RIGHT BULLET PATTERN)')
        else:
            print('Logging Values Disabled')


def RecoilControl(X, Y, Button, Pressed):   # Mouse-Thread
    """
    This Function Is Called Whenever Mouse Is Clicked.
    Usage : Sort Of A main() Function for Controlling Recoil (Creates Objects, And Calls Class Methods Whenever Mouse Is
            Clicked.
    """

    if Pressed and AntiRecoilEnabled:
        AntiRecoil = ValorantAntiRecoil(random.uniform(30, 35), Weapon, (X, Y))
        AntiRecoil.ManageRecoil()

    if Pressed and LoggingEnabled:
        CoorLogger((X, Y))

# ----------------------------------------------------------------------------------------------------------------------

def CoorLogger(ClickCoor):
    """
    MouseCoordinate Logger For Logging Successive Bullet Coordinates.
    """

    global RecoilPatternLog

    if len(RecoilPatternLog) < 10:
        RecoilPatternLog.append(ClickCoor)
        print('Bullets Logged = ', len(RecoilPatternLog))

    else:
        print(RecoilPatternLog)
        KeyboardController.press(pynput.keyboard.Key.f7)
        KeyboardController.release(pynput.keyboard.Key.f7)

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':  # Main-Thread

    Toggler = pynput.keyboard.Key.f1
    MouseController = pynput.mouse.Controller()
    KeyboardController = pynput.keyboard.Controller()
    AntiRecoilEnabled = False
    LoggingEnabled = False
    Weapon = 'VANDAL'
    RecoilPatternLog = None

    with pynput.mouse.Listener(on_click = RecoilControl) as MouseListener:
        with pynput.keyboard.Listener(on_press = AntiRecoilData) as KeyboardListener:   # Keyboard Listener Thread
            KeyboardListener.join()
            MouseListener.join()
