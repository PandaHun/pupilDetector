# pupilDetector

### 19'1'7' 시작

* 19'1'14' 눈 잡기 성공

  > *하지만 눈의 범위를 얼굴 외부에서도 잡고, 코와 입을 잡는 경우도 발생함* 
  >
  > 우선은 눈동자를 잡는 것이 중요함

* 19'1'16' 기계 $$Epsilon$$을 사용해서 눈의 중앙을 잡음. 

  > *하지만 간단한 수식으로 만든 점이라 정확도가 떨어짐*
  >
  > Edge Detection으로 정확한 값을 잡아야 할 것으로 생각됨

* 19'1'22' 14'의 문제점을 잡기 위해 검출한 얼굴의 내부에서만 눈을 잡도록 소스 수정

* 19'1'29' 눈동자를 잡는 것은 큰 아웃풋을 가져오지 못할 것으로 추정됨. 얼굴 전체 특징 점으로 
