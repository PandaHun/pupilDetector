import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

kerner_sharpen = np.array([[1,1,1],[1,-7,1],[1,1,1]])
output = cv2.filter2D(frame, -1, kerner_sharpen)

cv2.imshow('sharpening',output)
cv2.waitKey(0)