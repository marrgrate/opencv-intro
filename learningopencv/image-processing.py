#basics of image processing

#changing color-spaces
import cv2 as cv
import numpy as np
from config import PATH
from matplotlib import pyplot as plt

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
    lower_yel = np.array([50,50,50])
    upper_yel = np.array([90,200,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_yel, upper_yel)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()


#####################################################################
#Transformations
#resizing
img = cv.imread(PATH + 'lena.png')
res = cv.resize(img, None, fx=1, fy=0.5, interpolation = cv.INTER_CUBIC)
#OR
#height, width = img.shape[:2]
res = cv.resize(img,[200, 200], cv.INTER_CUBIC)

#shifting
rows, cols, channels = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#rotation
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)

#affine transformation
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

#perspective transformation
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[1100,100],[70,1000],[1100,1000]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()