import cv2
import matplotlib.pyplot as plt
# 이미지 합성해보자
# man / turket 이미지 생성(컬러)
src1 = cv2.imread('./man.jpg')
src2 = cv2.imread('./turkey.jpg')


# src1 + src2 값이 255를 넘어가면 해당값의 256을 빼서 표현
dst1 = src1 + src2 # +: 특정 밝기를 넘어서면 색상반전
# cv2.add(src1, src2)의 값이 55를 넘어가면 255로 고정
dst2 = cv2.add(src1, src2) # add: 최대값이 흰색

img = {'src1': src1, 'src2':src2, 'dst1':dst1, 'dst2':dst2}

for i, (k,v) in enumerate(img.items()):
    plt.subplot(2,2,i+1)
    # BGR이미지 -> RGB로 변경
    plt.imshow(v[:,:,::-1])
    plt.title(k)
plt.show()