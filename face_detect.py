import numpy as np
import cv2 as cv


face_detect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

people = ['Messi', 'Elon', 'Bezoz', 'Ryan', 'Canu']

#features = np.load("features.npy")
#labels = np.load("label.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img = cv.imread(r"C:\Users\taslim\Desktop\Asiwaju Projects\OpenCV\images\Ryan\Ryan Reynolds.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

faces_rect = face_detect.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_rof = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_rof)
    print(f"label = {label} with a confidence of {confidence}")

cv.imshow("Detected", img)

cv.waitKey(0)