import cv2
# dog이미지 컬러로
img = cv2.imread('./dog.bmp')
img_copy = img.copy() # 복사하면 서로 다른 공간을 할당함 -> 결과가 다르다!
# img_test = img # 할당하게 되면 같은 공간을 가리킴 -> 결과가 같다!

# print(img_copy.shape) 높이, 너비, 채널수
# 행(높이) - 91~210 / 열(너비)
img_copy[91:210, 125:245] = (244,102,255)

cv2.imshow('img', img)
cv2.imshow('img_copy', img_copy)

cv2.waitKey()



