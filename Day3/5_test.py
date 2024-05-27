import cv2

src = cv2.imread('./candies.png') # BGR
print('shape: ', src.shape)
print('dtype: ', src.dtype)

b = src[:,:,0]
g = src[:,:,1]
r = src[:,:,2]



cv2.imshow('src', src)
cv2.imshow('b', b) # 각 색상에 해당하는 부분이 흰색으로 보임
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey()
