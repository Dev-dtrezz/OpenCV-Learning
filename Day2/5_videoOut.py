import cv2
# 두개의 동영상을 읽어들어와서 하나의 영상으로 출력해보기

# 비디오객체 1,2 생성
cap1 = cv2.VideoCapture('./tiger.mp4')
cap2 = cv2.VideoCapture('./clouds.mp4')

# 영상의 총 프레임수 반올림
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_cnt1)
print(frame_cnt2)

# 1초당 프레임수 반환
fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)
print(fps1)
print(fps2)

# 영상의 가로, 세로
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('width', w)
print('height', h)

# VideoWriter객체 생성 , 코드포맷 방식 : Divx
fourcc = cv2.VideoWriter.fourcc(*'DIVX')
# 비디오 내보내기_파일명 / 코드포맷 객체 / 초당 fps / 프레임사이즈 튜플
out = cv2.VideoWriter('mix.avi', fourcc, fps1, (w,h))

# 총 프레임수를 돌면서 out객체에 write메서드로 frame을 넣어주기(영상 혼합)
for i in range(frame_cnt1):
    ret, frame = cap1.read() # 영상 읽어오기
    cv2.imshow('output', frame) # 츌력
    out.write(frame) # out객체에 frame 씌우기
    if cv2.waitKey(10) == 27:
        break

for i in range(frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow('output', frame)
    out.write(frame) # out객체에 frame 씌우기
    if cv2.waitKey(10) == 27:
        break

cap1.release()
cap2.release()
out.release()