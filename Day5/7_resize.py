import cv2
# 강아지_색상으로
img = cv2.imread('./dog.bmp')
# 크기변환1_가장 가까운 픽셀 값 사용
dst1 = cv2.resize(img, (1280, 1023), interpolation=cv2.INTER_NEAREST) # 속도는 빠르지만 퀄리티 낮음
# 크기변환2_인접한 16개 픽셀의 가중치 사용
dst2 = cv2.resize(img, (1280, 1023), interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
cv2.imshow('dst1', dst1[400:800,200:600]) # 일부추출
cv2.imshow('dst2', dst2[400:800,200:600])
cv2.waitKey()
# cubic이 더 퀄리티가 좋음
