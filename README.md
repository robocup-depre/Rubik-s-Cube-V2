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
## Solving

