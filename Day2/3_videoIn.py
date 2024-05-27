import cv2
import sys

# VideoCapture객체 생성
cap = cv2.VideoCapture('./tiger.mp4')

if not cap.isOpened():
    print('동영상을 열 수 없습니다')
    sys.exit()

print('동영상 연결 성공!')
print('가로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('프레임 수: ', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
print('FPS: ', cap.get(cv2.CAP_PROP_FPS))

# 비디오
while True:
    ret, frame = cap.read()
    # return에 실패하면 break 실행
    if not ret:
        break
    # frame값을 계속 반환
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27: # ESC
        break

cap.release()