import cv2
import math
# pts(외곽선)을 크기를 계산해 img에 바운딩박스를 그리고 제목을 붙임
def setLabel(img, pts, label):
    (x,y,w,h) = cv2.boundingRect(pts) # pts기준으로 최소크기의 사각형 계산
    pt1 = (x,y)
    pt2 = (x+w, y+h)
    cv2.rectangle(img, pt1, pt2, (0,0,255),2) # 사각형그리기
    # 이름추출
    cv2.putText(img,label,pt1,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))

# 도형객체 / 컬러로
img = cv2.imread('./polygon.bmp')
# 도형객체+흑백 이미지 생성(오츠이진화 사용)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 오츠이진화_배경이 흰색으므로 _INV사용
_, img_bin = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# 외곽선 추출(오츠 이진화 이미지 기반)_외곽선만_외곽선을 이루는 점 튜플로 반환
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


for pts in contours:
    # 외곽선(점)의 면적이 200이하면 지나침
    if cv2.contourArea(pts) < 200:
        continue
    # approx: 근사화하여 근소화된 꼭짓점 좌표를 튜플형태로 반환
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    # print(approx)
    vtc = len(approx) # 꼭짓점의 갯수계산
    print(vtc)

    if vtc == 3: #꼭짓점이 3이면 삼각형
        setLabel(img, pts, 'TRI')
    elif vtc == 4:
        setLabel(img, pts, 'RECT')
    else:
        # 길이와 면적으로 원인지 판단하여 원/기타로 구분
        length = cv2.arcLength(pts, True)
        area = cv2.contourArea(pts)
        ratio = 4. * math.pi * area / (length * length) # 원인지 판단공식

        if ratio > 0.70:
            setLabel(img, pts, 'CIR')
        else:
            setLabel(img, pts, 'NONAME')

cv2.imshow('img',img)
cv2.waitKey()

# 결과 : 외곽선을 계산하여 근사화(간소화)하여 꼭짓점을 구한 후 꼭짓점을 기준으로
# 형태를 파악하여 도형구분
