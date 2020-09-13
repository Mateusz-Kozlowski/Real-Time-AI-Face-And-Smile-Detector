# Real-Time-AI-Face-And-Smile-Detector

This file includes the following chapters:
1. Code Requirements
2. Project description
3. How to install
4. Tips

# 1. Code Requirements:
Python 3.8 with following modules installed:
* NumPy
* OpenCV 4.4 for Python
A webcam connected to your computer

# 2. Project Description:
The project is my modification of [Real Time AI Smile Detector](https://youtu.be/uLY5JSE5WAU).
It can recognize faces and smiles using the [haar algorithm](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html).
I used a ready-made model from the [openCV library github](https://github.com/opencv/opencv/tree/master/data/haarcascades)

Important note: the program can only be closed by pressing the escape key (it cannot be closed by clicking on the red X in the upper right corner of the window).

# 3. How to install:
If you're familiar with git you can clone the repo. Otherwise you can simply download whole project as a compressed folder.



Then you need to make sure your device meets the requirements in chapter 1 (appropriate libraries installed).
You can install them with pip from the command line.

Finally run the program using command line. Navigate to the directory, where the project is located and type python main.py



Wait a few second...
And you should see sth like that:



In the command line there may be some errors and warnings, but if you can use program and numbers are predicted correctly, then you can just ignore the erros.



If program doesn't work at all, read carefully the errors and try to find rezolution on Stack Overflow or elsewhere. You should necessarily make an issue in the repo too.

# 4. Tips:

