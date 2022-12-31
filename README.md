# Rubik-s-Cube-V2
This is a new version of [this](https://github.com/robocup-depre/Risolutore-del-Cubo-di-Rubik) project.
It is recommended to use a GAN cube (or another good brand) to minimize the risk of the motors blocking during movement(I used a GAN 356 Air M, but even a non-magnetic Cube will be OK).
## What's new
The first difference has to do with how the machine has to be used: in fact now you have to use a Telegram Bot to control the machine.
Another difference is about the scanning method: in the previous version you had to stick some [Apriltags](https://github.com/AprilRobotics/apriltag) on the cube to simplify the process, but now you won't need them anymore.
## About the scanning process
Now the programm searches only for the colors. This makes everything more convenient and simple, although it may be more error-prone due to ambient lighting. To solve this problem, every time a face recognition process is carried out, the bot also returns an image representing the recognized colors to the user, so that you can check at a glance if there have been any problems.
To scan a face of the cube it is sufficient to take a photo, possibly with sufficient lighting, and crop it so that the contours of the cube face roughly match those of the photo, and wait for the bot to send you the feedback picture. if you find there have been problems in the scanning process, you just have to send the photo again, improving the lighting and making sure you have carefully cropped the photo.
## Installation
Once you have a Raspberry Pi with the newest version of Raspberry Pi OS, it's time to install some packages.
Open a terminal and type:
```
sudo apt-get update
sudo apt-get upgrade -y
sudo reboot
```
Wait for the Pi to reboot.
Now install OpenCV:
```
sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y
sudo pip install opencv-python==4.6.0.66
```

Now check if there are any problems trying to run OpenCV:
```
sudo python3
>>> import cv2
>>> exit()
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
Now let's install [git](https://git-scm.com) and clone this repository into the /home folder:
```
sudo apt-get install git
sudo git clone https://github.com/robocup-depre/Rubik-s-Cube-V2.git
```
Make sure you have successfully created your own telegram bot, like explained in [this article](https://www.telegram-group.com/en/blog/create-bot-telegram).
Now it's time to edit one python scripts. Enter the Rubik-s-Cobe-V2 folder:
```
cd
cd Rubik-s-Cube-V2
```
Insert your Token in the code to link your bot to the code that will be executed in your Raspberry. I will use nano to do this, but you can also use an IDE like Idle, or even any test editor.
```
sudo nano Bot.py
```
Move to the 13° line, and write your Token rigth after __TOKEN=__.
Chose a password and write it in the 14° line, after __password=__.
Now type __Ctrl+S, Y, Enter__ to save the document.

The last thing to do is to make the Raspberry start the bot at boot using the [crontab](https://en.wikipedia.org/wiki/Cron) tool.
Type:
```
cd
mkdir logs
sudo crontab -e
```
You will be asked to chose a test editor (I recommend you to chose nano). Move to the bottom of the document, and write the following command:
```
@reboot sh /home/pi/Rubik-s-Cube-V2/startup_bot.sh >/home/pi/logs/cronlog 2>&1
```
Type __Ctrl+X, Y, Enter__ to save.

Now reboot.
```
sudo reboot
```
### If the bot doesn't start at boot
Chech the crontab's log:
```
cd
cd logs
ls
```
If you don't find a file called __cronlog__, you've probably skipped something, because it means that crontab has started nothing. Anyway, start from the beginning and reinstall all again (it will be faster).  
