import cv2
import matplotlib.pyplot as plt
# 히스토그램: 영상 픽셀값의 분포를 그래프 형태로 표현
# dog이미지생성(흑백)
src = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)

# calcHist_[영상], [히스토그램을 구할 채널], 빈의 갯수: 데이터구조를 몇개로 분할할지, 히스토그램의 최소/최대값
hist = cv2.calcHist([src], [0], None, [256], [0,255])

cv2.imshow('src',src)
plt.plot(hist)
plt.show()
cv2.waitKey()

# 결과: y축은 픽셀 / x축은 빈의갯수(0~255)를 가진 선그래프생성

