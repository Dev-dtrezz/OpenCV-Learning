import cv2

src = cv2.imread('./airplane.bmp')
mask = cv2.imread('./mask_plane.bmp')
dst = cv2.imread('./field.bmp')

cv2.copyTo(src, mask, dst)

cv2.imshow('src',src)

cv2.imshow('dst',dst)
cv2.waitKey()