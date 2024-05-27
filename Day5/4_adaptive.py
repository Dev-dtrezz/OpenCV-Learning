import cv2
import matplotlib.pyplot as plt
# 스도쿠 이미지_흑백으로
img = cv2.imread('./sudoku.jpg', cv2.IMREAD_GRAYSCALE)
# 이진화1_오츠이진화
th, dst1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 이진화2_적응형이진화_이웃픽셀의 평균으로
dst2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
# 이진화3_적응형이진화_가우시안분포에 따른 가중치의 합
dst3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)

dic = {'img':img, 'dst1':dst1, 'dst2':dst2, 'dst3':dst3}
# i:인덱스 / k:키(txt) / v:밸류
for i, (k,v) in enumerate(dic.items()):
    plt.subplot(2,2,i+1) # 2x2그리드에서 i+1번째 생성
    plt.title(k)
    plt.imshow(v, 'gray')

plt.show()

# 결과:가우시안 적응형이진화가 잡티가적음(선명도는 평균 적응형 이진화가 제일 좋음)