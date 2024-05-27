import cv2
import random
# 사진은 흑백으로
img = cv2.imread('./contours.bmp', cv2.IMREAD_GRAYSCALE)

# 검출모드:모든 외곽선/2단계 계층구조, 근사화:모든 외곽선 끝점의 좌표만 반환
contours, _ = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# print(contours)

# 색상변환_그레이스케일->BGR
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# 랜덤 색상 생성
color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
print(color)
# 외곽선 그리기_이미지:dst, 좌표:contours, 인덱스:-1(모두), 색상, 두께:3
cv2.drawContours(dst, contours, -1, color,3)

cv2.imshow('img', img)
cv2.imshow('dst',dst)
cv2.waitKey()

# 결과: 잡히는 모든 객체에 랜덤색상의 외곽선그림