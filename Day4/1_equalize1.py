import cv2
import matplotlib.pyplot as plt
# 흑백사진 이퀄라이즈

src = cv2.imread('./Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.equalizeHist(src) # 뭉쳐있는 정보를 펼쳐줌

hist1 = cv2.calcHist([src], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([dst], [0], None, [256], [0, 255])

hists = {'hist1': hist1, 'hist2': hist2}

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()

plt.figure(figsize=(12, 8))
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 2, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()