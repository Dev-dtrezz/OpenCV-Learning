import cv2
# cap이라는 VideoCapture객체 생성
cap = cv2.VideoCapture(0)

# frame가로사이즈 반환
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame세로사이즈 반환
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 1초당 프레임수 반환
fps = cap.get(cv2.CAP_PROP_FPS)

# 동영상 객체생성(fourcc) / DIVX확장자
fourcc = cv2.VideoWriter.fourcc(*'DIVX')
# 동영상 파일저장(파일명 / fourcc객체, fps, 프레임사이즈 튜플)
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()
out.release()