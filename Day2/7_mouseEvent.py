import cv2
import numpy as np

# 기존 x,y값 설정
oldx = oldy = 0

# 마우스 이벤트 함수
# event객체, x,y좌표, flags:버튼이 눌렸는지 떼졌는지 여부(불리언)
def onMouse(event, x, y, flags, param):
    # 전역변수 지정
    global oldx, oldy
    # print(event)
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼 눌릴 때
        # 전역변수에 좌표지정
        oldx, oldy = x, y
        print('왼쪽 버튼이 눌렸어요: %d, %d' % (x,y))

    elif event == cv2.EVENT_LBUTTONUP: # 왼쪽 버튼이 떼졌을 때
        print('왼쪽 버튼이 떼졌어요: %d, %d' % (x,y))
    elif event == cv2.EVENT_MOUSEMOVE: # 마우스 움직일때
        # 마우스가 눌린 상태+왼 버튼 눌린 상태
        if flags & cv2.EVENT_FLAG_LBUTTON:
            # 1차로 눌렸던 곳과 현재의 눌린 좌표에 라인 그리기
            cv2.line(img, (oldx,oldy), (x,y), (255,51,255), 3)
            cv2.imshow('img', img)
            # 좌표 할당
            oldx, oldy = x, y

# 컬러이미지 생성
img = np.ones((500,500,3), dtype=np.uint8) * 255
cv2.namedWindow('img') # 창의 이름을 지정

# 'img' 창에 마우스 콜백함수 지정
cv2.setMouseCallback('img', onMouse)

cv2.imshow('img', img)
cv2.waitKey()