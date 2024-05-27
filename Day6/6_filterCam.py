import cv2
import numpy as np
# 동영상 처리하기_0: 시스템의 기본카메라
cap = cv2.VideoCapture(0)

#함수생성
#가우시안블러링 적용함수_사이즈:자동계산(0,0)
def blur_filter(img):
    img = cv2.GaussianBlur(img, (0,0), 3)
    return img

# 캐니적용 함수(엣지검출)
def canny_filter(img):
    med_val = np.median(img)
    lower = int(max(0, 0.5*med_val))
    upper = int(min(255, 1.5 * med_val))
    dst = cv2.GaussianBlur(img, (3,3), 0, 0)
    dst = cv2.Canny(dst, lower, upper, 3)
    return dst
# 기본모드
cam_mode = 0

# 영상을 계속 돌림
while True:
    ret, frame = cap.read() # 리턴여부, 프레임
    if cam_mode == 1: # 가우시안블러링
        frame = blur_filter(frame)
    elif cam_mode == 2: # 캐니엣지검출
        frame = canny_filter(frame)
    cv2.imshow('frame', frame)
# 키 이벤트 설정
    key = cv2.waitKey(10)
    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0

cap.release()