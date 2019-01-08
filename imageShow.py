#Computer Vision을 위한 cv2 module을 불러옴
import cv2

#cv2.imread를 이용해 이미지를 읽어옴
#imread(fileName, flag)     이미지의 객체 행렬을 리턴함
#fileName은 상대 혹은 절대 경로를 사용
#flag는 이미지 파일을 읽을 때의 옵션을 나타냄 총 3가지
#cv2.IMREAD_COLOR(이미지를 컬러로 읽음 default) / cv2.IMREAD_GRAYSCALE(GrayScale로 읽는데 이미지 처리시 중간단계로)
#cv2.IMREAD_UNCHANGED
image = cv2.imread("./image/lunar.jpg", cv2.IMREAD_UNCHANGED)

#cv2.imshow는 이미지를 사이즈에 맞게 보여줌
#imshow(title, image)
#title은 보여주는 창의 title을, image는 cv2.imread의 return 값을 넣어줌
cv2.imshow("Moon", image)  

#waitkey()는 key 입력 대기함수
cv2.waitKey(0)
#모든 윈도우를 종료
cv2.destroyAllWindows()