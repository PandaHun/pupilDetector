#Pupil을 잡기위해선 조금 더 많은 경계를 잡아볼 필요가 있을 것 같다.
#Corner Detector 중 Harris Detector를 사용하자.

import cv2
import numpy as np

filename = './image/me.png'
img = cv2.imread(filename)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
for steps in range(100,500):
    dst = cv2.cornerHarris(gray, 2, 3, 1/steps)
    dst = cv2.dilate(dst, None)

    img[dst>0.01 *dst.max()] = [0,0,255]


    cv2.imshow('steps', img)
    if cv2.waitKey(0) & 0xff==27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)