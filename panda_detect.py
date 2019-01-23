import numpy as np
import cv2 
import sys

epsilon =sys.float_info.epsilon
#Variable for Casc filePath
faceCascPath = "C:/Users/Pandahune/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
eyeCascPath = "C:/Users/Pandahune/Anaconda3/Lib/site-packages/cv2/data/haarcascade_eye.xml"

#Get the Cascade Classifier
faceCascade = cv2.CascadeClassifier(faceCascPath)
eyeCascade = cv2.CascadeClassifier(eyeCascPath)

#frame = cv2.imread("./image/me.jpg", cv2.IMREAD_UNCHANGED)
#Module acts get the Video from webcam in laptop
try:
    capture = cv2.VideoCapture(0)
    #capture = cv2.VideoCapture("./image/me.mp4")
except:
    print('Failed Camera Load')

#Processing the Detector
while True:
    #Get the frame from the webcam
    ret, frame = capture.read()

    #For the processing the frame. so Convert the Color to gray
    gray_vid = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #filter the frame that canny edge
    filter = cv2.Canny(gray, 45, 45)

    #Detect the face using Cascade
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors =5,
        minSize = (180,180),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    eyes = eyeCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 10,
        minSize = (45,45),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    irises = []
    #Process that Detect Eyes
    dst = gray.copy()
    frame_crop = frame
    for (x,y, w, h) in faces:
        #print("Face Detected")

        frame_crop = frame[y:int(y+h*0.55), x:x+w]
        for (ex,ey,ew,eh) in eyes:
            if not (ex <x or ey < y or ey > y+h or ex > x+w):
                iris_w = int((ex+epsilon) + float((ew / 2)+epsilon))
                iris_h = int((ey+epsilon) + float((eh / 2)+epsilon))
                irises.append([np.float32(iris_w), np.float32(iris_h)])
                cv2.line(frame, (iris_w+2, iris_h), (iris_w-2, iris_h), (0,255,0), 2)
                cv2.line(frame, (iris_w, iris_h+2), (iris_w, iris_h-2), (0,255,0), 2)
            # cv2.line(frame, (x-2,y), (x+2, y), (0,255,0), 5)
            # cv2.line(frame, (x,y-2), (x, y+2), (0,255,0), 5)
            # cv2.line(frame, (x+w-2,y), (x+w+2, y), (0,255,0), 5)
            # cv2.line(frame, (x,y+h-2), (x, y+h+2), (0,255,0), 5)
    #    print(iris_w, iris_h)
        cv2.rectangle(frame, (x,y), (x+w, int(y+h*0.6)), (0,255,0), 1)
    #        cv2.circle(gray, (iris_w,iris_h),int(float((iris_h/32)+epsilon)), (0,255,0), 2)
    #        cv2.line(gray, (ex+3,ey), (ex, ey),(255,0,0),1)

    #Show the frame
    cv2.imshow('Original Video', frame)
    cv2.imshow('Croped Video', frame_crop)
    #cv2.imshow('Gray Video', gray)
    #cv2.imshow('Edge Video', filter)


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