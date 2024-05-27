import cv2
import numpy as np
# 누워있는 사진을 똑바로 펼침
img = cv2.imread('./pic.jpg')
# perspective 적용된 창 크기설정
w, h = 600,400

# 변경전->변경후 좌표 생성
srcQuad = np.array([[370,173],[1220,155],[1420,840],[210,850]], np.float32)
dstQuad = np.array([[0,0],[w,0],[w,h],[0,h]], np.float32)
# 투시변환 객체 생성_src좌표->dst좌표로 변환
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
# 투시변환 적용-영상:img / 변환행렬:pers, 결과영상크기:(w,h)
dst = cv2.warpPerspective(img, pers, (w,h))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey()