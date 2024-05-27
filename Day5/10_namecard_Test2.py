import cv2
import numpy as np

src = cv2.imread('./namecard.jpg')
# w,h = int(src.shape[1]*0.8),int(src.shape[0]*0.8)
# dst1 = cv2.resize(src,(w,h),interpolation=cv2.INTER_NEAREST)
x,y = int(src.shape[1]),int(src.shape[0])
# 원그리기
cv2.circle(src, (50,50), 25,(255,255,0),-1)
cv2.circle(src, (x-50,50), 25,(255,255,0),-1)
cv2.circle(src, (50,y-50), 25,(255,255,0),-1)
cv2.circle(src, (x-50,y-50), 25,(255,255,0),-1)
# 직선그리기

cv2.imshow('src',src)
cv2.waitKey()



