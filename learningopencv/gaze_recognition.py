import cv2 as cv
import numpy as np
#initialization for blob detection algorythm
detector_params = cv.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv.SimpleBlobDetector_create(detector_params)

face_classifier = cv.CascadeClassifier(r'C:\Users\maryia.grankouskaya\source\repos\opencv\opencv\env\Haarcascades\haarcascade_frontalface_default.xml')
eyes_classifier = cv.CascadeClassifier(r'C:\Users\maryia.grankouskaya\source\repos\opencv\opencv\env\Haarcascades\haarcascade_eye.xml')

def detectFaces(image, classifier):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    #make pic gray
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        print("no faces found")
    for (x,y,w,h) in faces:
        frame = img[y:y+h, x:x+w]
        return frame

def detectEyes(img, img_gray, classifier):
    coords = cascade.detectMultiScale(img_gray, 1,3, 5)
    height = np.size(img, 0)
    for (x, y, w, h) in coords:
        if y+h > height/2:      # pass if the eye is at the bottom
            pass

def detectEyes(img, classifier):
    gray_frame = cv.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5) # detect eyes
    width = np.size(image, 1) # get face frame width
    height = np.size(image, 0) # get face frame height
    left_eye = None
    right_eye = None
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # get the eye center
        if eyecenter < width * 0.5:
            left_eye = img[y:y + h, x:x + w]
        else:
            right_eye = img[y:y + h, x:x + w]
    return left_eye, right_eye

def cutEyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)
    return img


def blobProcess(img, detector):
    gray_frame = cv.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv.threshold(gray_frame, 42, 255, cv2.THRESH_BINARY)
    img = cv.erode(img, None, iterations=2) #1
    img = cv.dilate(img, None, iterations=4) #2
    img = cv.medianBlur(img, 5) #3
    keypoints = detector.detect(img)
    return keypoints


def cutEyebraws(eye_frame):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)
    return img

def main():
    image = cv.imread(r'C:\Users\maryia.grankouskaya\Desktop\lena.png')
    cv.namedWindow('face')
    cv.createTrackbar('threshold', 'face', 0, 255, nothing)
    face_frame = detectFaces(image, face_classifier)
    if face_frame is not None:
        eyes = detectEyes(face_frame, eyes_classifier)
        for eye_frame in eyes:
            if eye is not None:
                eye_frame = cutEyebraws(eye_frame)
                threshold = cv2.getTrackbarPos('threshold', 'image')
                keypoints = blobProcess(eye, threshold, detector)
                eye = cv.drawKeypoints(eye, keypoints, eye, (0,255,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imshow('face', face_frame)
    cv.waitKey(0)
    cv.destroyAllWindows()