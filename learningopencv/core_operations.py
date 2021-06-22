#core operations

#Access pixel values and modify them
#Access image properties
#Set a Region of Interest (ROI)
#Split and merge images

import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt
from config import PATH



img = cv.imread(r'C:\Users\maryia.grankouskaya\source\repos\learningopencv\learningopencv\env\sample\data\lena.png')
if os.path.isfile(r'C:\Users\maryia.grankouskaya\source\repos\learningopencv\learningopencv\env\sample\data\lena.png') == False:
    print('file not found')

px = img[100, 100, 2]
print(px)

img[100,100] = [255,255,255]
print(img[100,100])

#better using numpy
print(img.item(100,100,1))
#modifying
img.itemset((100,100,1), 50)
print(img.item(100,100,1))

#accessing image properties
print(img.shape)
print(img.size)
print(img.dtype)

eye = img[600:670, 580:680]
img[500:570,690:790] = eye


img = cv.resize(img, (512,512), cv.INTER_LINEAR)
cv.imshow("resized lena", img)

#Splitting and Merging Image Channels


BLUE = [255,0,0]

replicate = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()

##########################################################################
#ARITHMETIC OPERATIONS ON IMGS

#try out several arithmetic operations on images, like addition, subtraction, bitwise operations, and etc.
#functions: cv.add(), cv.addWeighted(), etc.
