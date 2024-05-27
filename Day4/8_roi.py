import cv2

img1 = cv2.imread('./sun.jpg')

# x, y, w, h
x = 182
y = 21
w = 122
h = 110

roi = img1[y:y+h,x:x+w]
img2 = roi.copy()

img1[y:y+h, x+w:x+w+w] = roi
cv2.rectangle(img1, (x,y), (x+w+w, y+h), (0,255,0), 3)

cv2.imshow('img1', img1)
cv2.imshow('roi', img2)
cv2.waitKey()