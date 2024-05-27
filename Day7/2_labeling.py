import cv2
# 키보드사진_흑백으로 불러오기
img = cv2.imread('./keyboard.bmp', cv2.IMREAD_GRAYSCALE)
# 오츠이진화_임계값:0(자동임계값 계산) / 최대값:255
_, img_bin = cv2.threshold(img,0,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 색상변경: 그레이스케일 -> BGR (흑백으로 구분 후 색상화)
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# 바운딩박스 갯수, 레이블맵 행렬 , 바운딩박스 정보, 무게중심 좌표
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin)
print("cnt: ",cnt) # 객체 갯수
print("labels: ",labels) # 레이블맵 행렬
print("stats: ",stats) # 크기: 폭, 높이, 면적 등 상태값
print("centroids: ",centroids) # 무게중심좌표

#바운딩 박스 객체 그려보기
#바운딩 박스 38개를 돌면서 30이상일때만 (좌표,폭,높이)가진 박스를 그림
for i in range(1, cnt):
    (x,y,w,h,area) = stats[i]
    if area < 30: #30보다작으면 처리를 건너뜀 -> 30이상만 사각형을 그림
        continue
    cv2.rectangle(dst, (x,y,w,h), (0,255,255))

cv2.imshow('img', img)
cv2.imshow('img_bin', img_bin)
cv2.imshow('dst', dst)
cv2.waitKey()

#결과 : 오츠이진화를 img_bin에 반환하고 dst에 검출된 객체에 바운딩박스 그림

