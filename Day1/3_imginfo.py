import cv2
'''
img_gray = cv2.imread('./dog.bmp',cv2.IMREAD_GRAYSCALE)
print('img_gray type:', type(img_gray))
print('img_gray shape:', img_gray.shape) # h / w 픽셀
print('img_gray dtype:', img_gray.dtype)

img_color = cv2.imread('./dog.bmp')
print('img_gray type:', type(img_color))
print('img_gray shape:', img_color.shape) # h / w 픽셀 채널 3개
print('img_gray dtype:', img_color.dtype)

# img_color의 정보를 아래와 같이 출력
# img_color 사이즈 : 548*364

img_color = cv2.imread('./dog.bmp')
# 개인 답안
he, wi, ch = list(img_color.shape)
print(f'img_color 사이즈: {wi}*{he}')
# 강사님 답안
h,w = img_color.shape[:2]
print(f'img_color 사이즈: {w}*{h}')
'''
# 문제2
# img_gray가 그레이스케일 영상인지 컬러 영상인지 구별하는 프로그램을 작성
# if문 사용
# img_gray는 그레이스케일 영상입니다
img_color = cv2.imread('./dog.bmp')
img_gray = cv2.imread('./dog.bmp',cv2.IMREAD_GRAYSCALE)
img = img_color
# 개인답안
# if len(img.shape) == 3:
#     print('img는 컬러 영상입니다')
# else:
#     print('img는 그레이스케일 영상입니다')
# 강사님답안
if len(img_gray.shape) == 2:
    print('img_gray 그레이스케일 영상입니다')
elif len(img_gray.shape) == 3:
    print('img_gray 컬러 영상입니다')
# 결과: 컬러영상은 shape(채널, 너비, 높이) 이기 때문에 3이다

# 문제3
# img_color 특정 색 정보로 영상을 출력
# BGR: (255,102, 255)
img_color = cv2.imread('./dog.bmp')
# 개인답변 - 더 좋은 답안
img_color[:,:] = (255,102, 255)
# nparray에 같은 데이터(색상 넣어주기)

'''
# 강사님
for x in range(h):
    for y in range(w):
        img_color[x,y] = (255,102,255)
'''

cv2.imshow('img', img_color) # 창이름, 영상
cv2.waitKey() # 키를 입력할 때까지 계속 대기



