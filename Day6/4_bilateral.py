import cv2
# 가우시안 노이즈_흑백으로 불러오기
img = cv2.imread('./gaussian_noise.jpg', cv2.IMREAD_GRAYSCALE)
# 블러1_가우시안블러적용_커널사이즈:(5,5), 표준편차:1
dst1 = cv2.GaussianBlur(img, (5,5),1)
# 블러2_바이레터럴 필터적용
dst2 = cv2.bilateralFilter(img, 5, 80, 80)

cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey()

# 결과: 가우시안필터에 비해 바이레터럴 필터의 경계가 또렷!