#basics of image processing

#changing color-spaces
import cv2 as cv
import numpy as np
from config import PATH

img = cv.imread(PATH)
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print("flags", flags)

#Object Tracking
cap = cv.VideoCapture(PATH + "color.mp4")

while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_yel = np.array([30,129,182])
    upper_yel = np.array([97,198,253])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_yel, upper_yel)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()