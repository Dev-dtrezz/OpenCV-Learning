import cv2
import random
import numpy as np
# 우유이미지 흑백으로(오츠이진화를 위함)
img = cv2.imread('./milkdrop.bmp', cv2.IMREAD_GRAYSCALE)
# 오츠이진화_임계값:0(자동), 최대값:255
_, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 외곽선 검출_모든 외곽선(2단계), 근사화: 모든외곽선 좌표저장
# contours : 외곽선을 구성하는 점들의 좌표 저장(튜플로 저장)
contours, _ = cv2.findContours(img_bin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# 이미지 h,w반영(색상채널 제거)
h,w = img.shape[:2]
# 3차원 구조의 검은 영역 만듦
dst = np.zeros((h,w,3), np.uint8)
# 외곽선 배열점(튜플)들을 돌면서 외곽선 생성
for i in range(len(contours)):
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    cv2.drawContours(dst, contours, i, color, 2)

cv2.imshow('img', img)
cv2.imshow('img_bin',img_bin)
cv2.imshow('dst',dst)
cv2.waitKey()

# 결과: 튜플을 돌면서 검출한 외곽선 마다 외곽선을 그림