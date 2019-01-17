import numpy as np
import cv2 
import sys

epsilon =sys.float_info.epsilon
#Variable for Casc filePath
#faceCascPath = "C:/Users/Pandahune/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
eyeCascPath = "C:/Users/Pandahune/Anaconda3/Lib/site-packages/cv2/data/haarcascade_eye.xml"

#Get the Cascade Classifier
#faceCascade = cv2.CascadeClassifier(faceCascPath)
eyeCascade = cv2.CascadeClassifier(eyeCascPath)

#Module acts get the Video from webcam in laptop
try:
    capture = cv2.VideoCapture(0)
except:
    print('Failed Camera Load')

#Processing the Detector
while True:
    #Get the frame from the webcam
    ret, frame = capture.read()

    #For the processing the frame. so Convert the Color to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detect the face using Cascade
    eyes = eyeCascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 10,
        minSize = (45,45),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    irises = []
    for (ex,ey,ew,eh) in eyes:
        iris_w = int((ex+epsilon) + float((ew / 2)+epsilon))
        iris_h = int((ey+epsilon) + float((eh / 2)+epsilon))
        irises.append([np.float32(iris_w), np.float32(iris_h)])

        print(iris_w, iris_h)

        cv2.rectangle(gray, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)

    
    #cv2.imshow('Original Video', frame)
    cv2.imshow('Gray Video', gray)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        capture.release()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        break

# # left_eye_x = eyes[0,0]
# # left_eye_y = eyes[0,1]
# # right_eye_x = eyes[1,0]
# # right

# print(eyes[0,1])