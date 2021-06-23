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
print('shape ' , img.shape)
print('size ' , img.size)
print('data type ', img.dtype)

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

x = np.uint8([250])
y = np.uint8([10])
print( cv.add(x,y) ) # 250+10 = 260 => 255
print(x+y)

img1 = cv.imread(PATH + '5.jfif')
if os.path.isfile(PATH + '5.jfif') == False:
    print('file 3 not found')


img2 = cv.imread(PATH + 'lena.png')
if os.path.isfile(PATH + 'lena.png') == False:
    print('file 4 not found')

img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]), cv.INTER_LINEAR)

print(img1.shape, img2.shape)
dst = cv.addWeighted(img1,0.5,img2,0.5,0)
cv.imshow('blending',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#img2 = cv.rotate(img2, cv.ROTATE_90_CLOCKWISE)
#Bitwise operations
img1 = cv.imread(PATH + '5.jfif')
img2 = cv.imread(PATH + 'logo.png')
img1 = cv.resize(img1, (512,512), cv.INTER_CUBIC)
img2 = cv.resize(img2,(100,100), cv.INTER_LINEAR)
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()

#Performance Measurement and Improvement Technique
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
cv.imshow('blur',img1)
print( t )