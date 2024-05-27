import cv2
# 밝기조절해보자
# dog이미지_흑백/컬러로 생성
src1 = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('./dog.bmp')

# 이미지 보이기
cv2.imshow('src1', src1)
cv2.imshow('src2', src2)

# 밝기 높이기(더하기)_흑백/컬러 방식 다름
dst1 = cv2.add(src1, 100)
dst2 = cv2.add(src2, (100,100,100,0)) # 가장 뒤는 채널이라서 더하면 x
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

# 밝기 낮추기(빼기)
dst3 = cv2.subtract(src1, 100)
cv2.imshow('dst3',dst3)

# 밝기 더하기(곱하기)
dst4 = cv2.multiply(src1, 10)
cv2.imshow('dst4',dst4)
# 밝기 낮추기(나누기)
dst5 = cv2.divide(src1, 10)
cv2.imshow('dst5',dst5)


cv2.waitKey()