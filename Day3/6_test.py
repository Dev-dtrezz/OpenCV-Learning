import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./dog.bmp')

b, g, r = cv2.split(src) # 채널 분리

hist = cv2.calcHist([b, g, r], [0], None, [256], [0,255])

cv2.imshow('src',src)
plt.plot(hist[0], color='blue')
plt.plot(hist[1],color='green')
plt.plot(hist[2])
plt.show()
cv2.waitKey()
