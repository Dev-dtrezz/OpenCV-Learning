import cv2
import numpy as np

# man/tureky이미지 생성(컬러)
src1 = cv2.imread('./man.jpg')
src2 = cv2.imread('./turkey.jpg')
# 가중치의 합을 활용하여 두 개의 영상을 합쳐보자
# 투명도 지정
alpha = 0.7

# 투명도를 활용하여 합치기
dst1 = src1 * alpha + src2 * (1-alpha)
dst1 = dst1.astype(np.uint8)

# 가중치의 합_가감할 상수(gamma):0
dst2 = cv2.addWeighted(src1, alpha, src2, (1-alpha), 0)

cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey()