import cv2
from matplotlib import pyplot as plt
# absdiff를 활용하여 영상간의 차이를 비교보자
# dog, square 이미지 생성(컬러)
src1 = cv2.imread('./dog.jpg')
src2 = cv2.imread('./square.bmp')

# 투명도 지정
alpha = 0.5

dst1 = cv2.add(src1, src2) # 최대값 255:흰색
dst2 = cv2.addWeighted(src1, alpha, src2, (1-alpha), 0) # 강아지50 : 흰색50
dst3 = cv2.subtract(src1, src2) # 최소값 0: 검은색
dst4 = cv2.absdiff(src1, src2) # -값을 +로 반전해서 값 추출(절대값)

img = {'dst1':dst1, 'dst2':dst2,'dst3':dst3, 'dst4':dst4}

for i, (k,v) in enumerate(img.items()):
    plt.subplot(2,2,i+1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
plt.show()
'''
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)

cv2.waitKey()
'''