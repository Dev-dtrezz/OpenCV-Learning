import cv2
# 강아지 사진_흑백으로
img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
# 가우시안블러링_커널사이즈:(0,0)_자동계산됨 , sigmaX(표준편차):1 높을수록 블러강함
dst1 = cv2.GaussianBlur(img, (0,0), 1)
# 표준블러링
dst2 = cv2.blur(img, (3,3))

cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey()

# 결과: 가우시안 분포가 더 원본과 가까우면서 노이즈삭제됨