import cv2
# 노이즈있는 사진_흑백으로 불러옴
img = cv2.imread('./noise.bmp', cv2.IMREAD_GRAYSCALE)
# 미디언블러러링_커널사이즈:3
dst = cv2.medianBlur(img, 3)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()

# 결과: 소금후추 노이즈가 잘 사라짐