import cv2
import numpy as np
# 쌀알이미지_흑백으로
src = cv2.imread('./rice.png', cv2.IMREAD_GRAYSCALE)

# 오츠 이진화 : 자동 임계값잡아서 이진화
_, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 이진화
# src와 같은 구조를 가지고 0으로 채워진 이미지 생성
dst2 = np.zeros(src.shape, np.uint8)
# 너비의 4등분의 몫을 반환_128
bw = src.shape[1] // 4
# 높이의 4등분의 몫을 반환_128
bh = src.shape[0] // 4

# 128로 등분된 지역을 4번씩 오츠이진화
for y in range(4):
    for x in range(4):
        src_ = src[y*bh: (y+1)*bh, x*bw: (x+1)*bw] # x,y:0기준 [0:128,0:128]영역
        dst_ = dst2[y*bh: (y+1)*bh, x*bw: (x+1)*bw]
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

# 오츠이진화 / 지역이진화 비교했을 때 지역 이진화의 노이즈가 적어짐