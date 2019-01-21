""" import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
left_corner = 0
rigtht_corner = 0

th_value = 5

def threshoding(value):
    global left_corner
    global rigtht_corner

    if (value<=54):
        left_corner = left_corner+1

        if(left_corner>th_value): 
            print('RIGHT')
            left_corner=0
    elif(value>54):
        rigtht_corner = rigtht_corner+1

        if(rigtht_corner>th_value):
            print('LEFT')
            rigtht_corner=0

while 1:
        ret, frame = cap.read()
        cv2.line(frame, (320,0), (320,480), (0,200,0),2)
        cv2.line(frame, (0,200), (640,200), (0,200,0),2)
        if ret ==True:
            col = frame

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            pupilFrame = frame
            clahe = frame
            blur = frame
            edge = frame
            eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
            detected = eyes.detectMultiScale(frame, 1.3,5)
            for (x,y,w,h) in detected:
                cv2.rectangle(frame, (x,y), ((x+w,y+h)), (0,0,255), 1)
                cv2.line(frame, (x,y), ((x+w,y+h)), (0,0,255), 1)
                cv2.line(frame, (x+w,y), ((x,y+h)), (0,0,255), 1)
                pupilFrame = cv2.equalizeHist(frame[y:(y+h), x:(x+w)])
                cl1 = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                clahe = cl1.apply(pupilFrame)
                blur = cv2.medianBlur(clahe, 7)
                circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=7, maxRadius=21)
                if circles is not None:
                    circles = np.round(circles[0,:]).astype("int")
                    print('interger', circles)
                    for(x,y,r) in circles:
                        cv2.circle(pupilFrame, (x,y), r, (0,255,255), 2)
                        cv2.rectangle(pupilFrame, (x-5,y-5), (x+5,x+5), (0,128,255), -1)
                        threshoding(x)
            cv2.imshow('image', pupilFrame)
            cv2.imshow('clahe', clahe)
            cv2.imshow('blur', blur)

            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
cap.release()
cv2.destroyAllWindows()
 """

import math
import cv2
import numpy as np

img = cv2.imread('./image/people.jpg')
scaling_factor = 0.7

img  = cv2.resize(img, None,fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
cv2.imshow('Input', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
img_1, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    area = cv2.contourArea(contour)
    rect = cv2.boundingRect(contour)
    x,y,w,h = rect
    radius = 0.25*(w+h)
    area_condition = (100 <= area <= 200)
    symmetry_condition = (abs(1- float(w)/ float(h)) <=0.2)
    fill_condition = (abs(1- (area/ (math.pi*math.pow(radius,2.0))) <= 0.3))
    if area_condition and symmetry_condition and fill_condition:
        cv2.circle(img, (int(x+radius), int(y+radius)), int(1.3*radius), (0,180,0), -1)
cv2.imshow('Pupil', img)
c = cv2.waitKey()
cv2.destroyAllWindows()