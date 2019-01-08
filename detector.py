import cv2
import numpy as np

faceCascPath = "C:/Users/Pandahune/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
eyeCascPath = "C:/Users/Pandahune/Anaconda3/Lib/site-packages/cv2/data/haarcascade_eye.xml"

faceCascade = cv2.CascadeClassifier(faceCascPath)
eyeCascade = cv2.CascadeClassifier(eyeCascPath)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors =5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        video.realease()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        break
