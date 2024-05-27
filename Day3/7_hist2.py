import cv2
import matplotlib.pyplot as plt
# dog컬러이미지 생성
src = cv2.imread('./dog.bmp')
# b,g,r순서의 채널을 가진 배열로 분리
bgr = cv2.split(src)

# 그래프 선 색상
colors = ['b', 'g', 'r']
# b/g/r 히스토그램 생성
for (b,c) in zip(bgr, colors):
    hist = cv2.calcHist([b], [0], None, [256], [0,256])
    plt.plot(hist, color=c)


cv2.imshow('src', src)
plt.show()
cv2.waitKey()
# b/g/r에 대해서 각 색상별로 히스토그램생성