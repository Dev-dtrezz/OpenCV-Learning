import cv2
import numpy as np

# # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
# print(kernel)
# 서킷이미지_흑백으로
img = cv2.imread('./circuit.bmp', cv2.IMREAD_GRAYSCALE)
# 모폴로지_사각형 생성_반드시 정방행렬은 아님
gse = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3)) # 무조건 정방행렬X
# 모폴로지처리_침식+사각형
dst1 = cv2.erode(img,gse)
# 모폴로지처리_팽창+사각형
dst2 = cv2.dilate(img,gse)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

# 결과_ 침식: 선이 얇아지고 배경이 많아짐, 팽창: 선이 두꺼워지고 내부 구멍이 작아짐

