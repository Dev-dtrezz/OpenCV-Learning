import cv2
import numpy as np

# 높이500 / 너비500 / 3개의 채널가지고 값을 255로 채움
img = np.full((500,500,3), 255, np.uint8)

# 시작점(70,70)튜플 -> 끝점(250,70), 색상:빨강(BGR) ,두께5
cv2.line(img, (70,70), (250,70), (0,0,255), 5)

cv2.rectangle(img, (50,200,150,100),(0,255,0),3)
cv2.circle(img, (300,100), 50,(255,255,0),-1)

str = 'Hello OpenCV!'
# 넣을 이미지, 넣을 문자, 넣을 좌표, 글꼴, 폰트크기, 색상
cv2.putText(img, str, (30,300), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))

cv2.imshow('img',img)
cv2.waitKey()