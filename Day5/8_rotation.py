import cv2

img = cv2.imread('./dog.bmp')
# 중심좌표 구하기_w/2, h/2
cp = (img.shape[1]/2, img.shape[0]/2) # 중심좌표 구하기
# 회전객체 생성_각도30도 / 비율0.5배
rot = cv2.getRotationMatrix2D(cp, 30, 0.5)
# 이미지 회전 적용
dst = cv2.warpAffine(img, rot, (0,0))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()