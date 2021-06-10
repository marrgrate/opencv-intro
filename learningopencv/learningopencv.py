import cv2 as cv
import sys
from PIL import Image

path = "C:\\Users\maryia.grankouskaya\source\repos\learningopencv\learningopencv\myenv\sample\data"
cv.samples.addSamplesDataSearchPath(path)
img = cv.imread(cv.samples.findFile("lena.jpg"))

if img is None:
    sys.exit("Could not read the image.") 
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("lena.png", img)
