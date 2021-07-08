import cv2 as cv
import numpy as np
import os
#from config import PATH

#initialization for blob detection algorythm
detector_params = cv.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv.SimpleBlobDetector_create(detector_params)

face_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")

def nothing(x):
    pass

def detectFaces(img, classifier):
    gray_frame = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    coords = classifier.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    for (x, y, w, h) in biggest:
        frame = img[y:y + h, x:x + w]
    return frame

def detectEyes(img, img_gray, classifier):
    coords = cascade.detectMultiScale(img_gray, 1,3, 5)
    height = np.size(img, 0)
    for (x, y, w, h) in coords:
        if y+h > height/2:      # pass if the eye is at the bottom
            pass

def detectEyes(image, classifier):
    gray_frame = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    eyes = classifier.detectMultiScale(gray_frame, 1.3, 5) # detect eyes
    width = np.size(image, 1) # get face frame width
    height = np.size(image, 0) # get face frame height
    left_eye = None
    right_eye = None
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # get the eye center
        if eyecenter < width * 0.5:
            left_eye = image[y:y + h, x:x + w]
        else:
            right_eye = image[y:y + h, x:x + w]
    return left_eye, right_eye

def cutEyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)
    return img

def blobProcess(img, threshold, detector):
    gray_frame = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img = cv.threshold(gray_frame, threshold, 255, cv.THRESH_BINARY)
    img = cv.erode(img, None, iterations=2)
    img = cv.dilate(img, None, iterations=4)
    img = cv.medianBlur(img, 5)
    keypoints = detector.detect(img)
    print(keypoints)
    return keypoints

def cutEyebraws(eye_frame):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)
    return img

def main():
    img = cv.imread(r'C:\Users\maryia.grankouskaya\source\repos\learningopencv\learningopencv\env\sample\data\4.jpeg')
    cv.namedWindow('image')
    cv.createTrackbar('threshold', 'image', 0, 255, nothing)
    while True:
        face_frame = detectFaces(img, face_classifier)
        if face_frame is not None:
            eyes = detectEyes(face_frame, eyes_classifier)
            for eye in eyes:
                if eye is not None:
                    threshold = cv.getTrackbarPos('threshold', 'image')
                    eye = cutEyebrows(eye)
                    keypoints = blobProcess(eye, threshold, detector)
                    eye = cv.drawKeypoints(eye, keypoints, eye, (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv.imshow('image', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()