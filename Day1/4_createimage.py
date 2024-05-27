import cv2
import numpy as np

img1 = np.empty((240,320), dtype=np.uint8) # 픽셀 사이즈 / 그레이스케일
img2 = np.zeros((240,320,3), dtype=np.uint8) # 전체 0인 컬러
img3 = np.ones((240,320), dtype=np.uint8) * 120 # 밝기정보 1 * 120 = 120
img4 = np.full((240,320,3), (255,102,255), dtype=np.uint8) # 색상정보


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()