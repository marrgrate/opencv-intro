import cv2 as cv
import sys
import os

path = r'C:\Users\maryia.grankouskaya\Desktop\lena.png'
print(os.path.isfile(path)) 
img = cv.imread(path, -1)

if img is None:
    sys.exit("Could not read the image.") 
cv.imshow("LENA", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("lena.png", img)

