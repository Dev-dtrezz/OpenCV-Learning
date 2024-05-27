import cv2
import numpy as np
# 강아지 사진_컬러로 불러오기
img = cv2.imread('./dog.bmp')

# [[1,0,a],[0,1,b]] - 이동 변환행렬(x방향으로 a만큼, y방향으로 b만큼)
aff = np.array([[1,0,150],[0,1,100]], dtype=np.float32) # 변환행렬 생성
# 영상:img / 변환행렬:aff / 결과영상:(0,0)_입력이미지와 동일하게
dst = cv2.warpAffine(img, aff, (0,0))

cv2.imshow('src', img)
cv2.imshow('dst',dst)
cv2.waitKey()