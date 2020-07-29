# 🔶 d3adsh0t !! 🔶


![](/samples/d3adsh0t.png)


**︻デ═一 Neural Network Aim-Bot for First-Person-Shooting Games in Python ︻デ═一**

## Disclaimer :

**'d3dsh0t' is a FPS Game Aimbot, It is purely experimental and is intended only for educational purposes.**

**Aimbots are cheats and illegal in games. This repo is solely for educational purposes only.**

Since this repo is open source (available to everyone), its just one google search away from cheaters abusing it, and I am not a fan of cheating in 'online multiplayer games', so I wont be uploading my weights for the model, also in game its able to **Process Detections** at around 35 - 40 frames per seconds, this drops to around 25 - 28 (40+ recommended in online games) frames per second when the Main-Thread waits for Cursor Movement when an enemy is detected (Combo-Key On Hold) on a **Overclocked 1080Ti**, so it wouldn't be top level and anyways wouldn't give that of an advantage, unless its re-written in C++ to optimize many parts. (maybe an increase in about 5-8 FPS ?! or more ?!)

I have no intentions on re-writting d3adsh0t in C++, I could have built the project in C++ only, (would have taken a bit more of time, deploying the model would be delayed, people could abuse it in 'online games' and a lot of other stuff) considering all that I chose not to (kinda intentionally handicaped my project)

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
Python Wrapper :           https://github.com/dc740/AutoHotPy

NOTE : Managing' Mouse-Inputs' depends on the game, normally games patch many mouse_events and movements,
So I resorted to this driver, if you dont know what you are doing when using this driver I highly recommend
you not to use it, because if not codedroperly in rare cases you could damage your PC, and I am not responsible
for any damage done to your computer, although if you dont tweak my code w.r.t that driver in 'd3adsh0t.py'
you should be fine.
```

## 'd3adsh0t' In Action :

![](/samples/example_1_d3adsh0t.gif)

![](/samples/example_2_d3adsh0t.gif) 
