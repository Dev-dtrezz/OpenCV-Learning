import cv2
import matplotlib.pyplot as plt
'''
# cv2를 통해 출력
img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
cv2.waitKey()

# matplotlib을 통해 그레이스케일 출력
img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off')
plt.imshow(img, cmap='gray')
plt.show()


img = cv2.imread('./dog.bmp')
plt.axis('off')
plt.imshow(img)
plt.show()

# matplotlib을 통해 트루컬러 출력(cvtColor 사용)
img = cv2.imread('./dog.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(img)
plt.show()
'''
# dog이미지 읽어오기 -> 그레이스케일
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
# dog이미지 읽어오기 -> 컬러
img_color = cv2.imread('./dog.bmp')
# BGR -> RGB 이미지 변경
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

# 1행 2열 1번째
plt.subplot(121)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')
# 1행 2열 2번째
plt.subplot(122)
plt.axis('off')
plt.imshow(img_color)
plt.show()