# Rubik-s-Cube-V2
[Still a work in progress...]
This is a new version of [this](https://github.com/robocup-depre/Risolutore-del-Cubo-di-Rubik) project.
It is recommended to use a GAN cube (or another good brand) to minimize the risk of the motors blocking during movement(I used a GAN 356 Air M, but even a non-magnetic Cube will be OK).
## What's new
The first difference has to do with how the machine has to be used: in fact now you have to use a Telegram Bot to control the machine.
Another difference is about the scanning method: in the previous version you had to stick some [Apriltags](https://github.com/AprilRobotics/apriltag) on the cube to simplify the process, but now you won't need them anymore.
## Scanning
Now the programm searches only for the colors. This makes everything more convenient and simple, although it may be more error-prone due to ambient lighting. To solve this problem, every time a face recognition process is carried out, the bot also returns an image representing the recognized colors to the user, so that you can check at a glance if there have been any problems.
To scan a face of the cube it is sufficient to take a photo, possibly with sufficient lighting, and crop it so that the contours of the cube face roughly match those of the photo, and wait for the bot to send you the feedback picture. if you find there have been problems in the scanning process, you just have to send the photo again, improving the lighting and making sure you have carefully cropped the photo.
## Installation
Once you have a Raspberry Pi with the newest version of Raspberry Pi OS, it's time to install some packages.
Open a terminal and type:
```
sudo apt-get update
sudo apt-get upgrade -y
```

Now install OpenCV:
```
sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y
sudo pip install opencv-python==4.6.0.66
```

Now check if there are any problems trying to run OpenCV:
```
sudo python3
>>>import cv2
>>>exit()
```

If you've got some error messages, try this(it should work...):
```
pip install -U numpy
```

Now install the kociemba library:
```
sudo pip install kociemba
```

Install the pyTelegramBotAPI library:
```
sudo pip install pyTelegramBotAPI
```
