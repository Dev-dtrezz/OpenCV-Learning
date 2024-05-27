import cv2
import numpy as np
# 강아지사진_컬러로
img = cv2.imread('./dog.bmp')

# img_ndarray 값중 중간값(평균x)_129
med_val = np.median(img)
# 129*0.7 / 0 중에서 최대값 구한 후 정수반환
lower = int(max(0, 0.7*med_val))
# 129*1.3 / 255 중에서 최소값 구한 후 정수반환
upper = int(min(255, 1.3*med_val))
print(med_val)
print(lower)
print(upper)
# 가우시안 블러 적용
dst = cv2.GaussianBlur(img, (3,3), 0, 0)
# 캐니엣지검출 적용
dst = cv2.Canny(dst, lower, upper, 3) # 낮출수록 잘게들어간 선 / 높일수록 큼직하게 선

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey()
