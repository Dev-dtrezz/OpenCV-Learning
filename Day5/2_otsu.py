import cv2
# 쌀알 이미지_흑백으로 가져오기
src = cv2.imread('./rice.png', cv2.IMREAD_GRAYSCALE)
# 자동으로 임계값 잡아주는 오츠알고리즘(th를 어떻게 잡았나 프린트)
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(th)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 자동으로 임계값(131.0)으로 잡아서 이진화 수행
# but 이상한 노이즈 발생하는 문제
