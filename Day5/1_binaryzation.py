import cv2
import matplotlib.pyplot as plt
# 세포사진은 흑백으로 불러오기
src = cv2.imread('./cells.png', cv2.IMREAD_GRAYSCALE)
# 히스토그램 그리기_영상:src ,채널인덱스:[0](흑백), 마스크:NONE, 빈의갯수:256, 히스트범위
hist = cv2.calcHist([src], [0], None, [256], [0,255])

# 임계값보다 낮으면 검정 / 높으면 흰색(_: 설정한 thresh 값)
_, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY) # 임계값 / 결과물
_, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)


cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)

plt.plot(hist)
plt.show()
cv2.waitKey()

# 결과: dst2의 임계값이 높기 때문에 검정으로 잡힌 이미지가 더 많다