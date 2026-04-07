import os
import cv2 as cv
import numpy as np

people = ['Messi', 'Elon', 'Bezoz', 'Ryan', 'Canu']


DIR = r'C:\Users\taslim\Desktop\Asiwaju Projects\OpenCV\images'
face_detect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rect = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h)in face_rect:
                faces_rof = gray[y:y+h, x:x+w]
                features.append(faces_rof)
                labels.append(label)

create_train()

print("Training Done......")


features= np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)

face_recognizer.save("face_trained.yml")
np.save('features.npy', features)
np.save('labels.npy', labels)