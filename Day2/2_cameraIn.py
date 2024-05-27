import cv2
import sys
# 카메라를 여는 방법_기본카메라:0 / 별도의 카메라는 고유의 INDEX값(VideoCapture객체생성)
cap = cv2.VideoCapture(0)

# 카메라에 연결되었는지(True:성공)
if not cap.isOpened():
    print('카메라를 열 수 없습니다')
    sys.exit() # 카메라 종료

print('카메라 연결 성공!')
print('가로사이즈', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) # 가로
print('세로사이즈', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) # 세로

while True:
    # ret:리턴되었는지여부(True) frame:카메라의 프레임
    ret, frame = cap.read()
    # 리턴이 안되었으면 종료
    if not ret:
        break
    # frame을 출력하기
    cv2.imshow('frame', frame)
    # 10ms마다 입력을 확인하면 esc(27)이 눌리면 종료
    if cv2.waitKey(10) == 27: # ESC
        break
# VideoCapture객체 해제 : 카메라 연결해제
cap.release()