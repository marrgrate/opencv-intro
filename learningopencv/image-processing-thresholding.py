#simple thresholding

from config import PATH
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread(PATH + 'lena.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

ret, t1 = cv.threshold(gray, 127,255, cv.THRESH_BINARY)
ret, t2 = cv.threshold(gray, 127,255, cv.THRESH_BINARY_INV)
ret, t3 = cv.threshold(gray, 127,255, cv.THRESH_TRUNC)
ret, t4 = cv.threshold(gray, 127,255, cv.THRESH_TOZERO)
ret, t5 = cv.threshold(gray, 127,255, cv.THRESH_TOZERO_INV)

titles = ['original', 'binary', 'bin inversed', 'truncate', 'tozero', 'tozero inversed']
images = [gray, t1,t2,t3,t4,t5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show();

#adaptive
#src.create(rows, cols, CV_8UC1)
#src = cv.imread(img, CV_8UC1)
adapt_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 17, 2)
adapt_gauss = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 17, 2)

titles = ['original', 'binary(v=127)', 'adaptive mean', 'adaptive gaussian']
images = [gray, t1, adapt_mean, adapt_gauss]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

#Otsu's Binarization
img = cv.imread(PATH + 'noisy-lena.jfif', cv.IMREAD_GRAYSCALE)
if img is None: 
    print("None image")
# global thresholding
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()