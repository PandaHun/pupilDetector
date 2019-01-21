import cv2

capture = cv2.VideoCapture(0)   #내장 혹은 외장 카메라에서 영상을 받아옴


#카메라의 속성을 설정
#captrue.set(option, n)
#option은 프레임의 너비와 높이의 속성 설정
#n이 설정할 값에 해당
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 

while True: #영상 출력을 위해
    ret, frame = capture.read() #capture.read()로 상태와 프레임을 받아옴
    cv2.imshow("VideoFrame", frame) #img를 보여주면서 띄움
    if cv2.waitKey(1) > 0: break


cv2.waitKey(0)
cv2.destroyAllWindows()