import cv2
# 색상별로 흰색으로 반환
# cadies이미지 생성(BGR)
src = cv2.imread('./candies.png') # BGR
print('shape: ', src.shape)
print('dtype: ', src.dtype)

b, g, r = cv2.split(src) # 채널 분리
'''
# ndarray 인덱싱 활용 - 채널
b = src[:,:,0]
g = src[:,:,1]
r = src[:,:,2]
'''
cv2.imshow('src', src)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey()

# 결과: 각 색상에 해당하는 부분이 흰색으로 보임