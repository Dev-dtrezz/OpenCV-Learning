import cv2

# dog이미지 컬러로 불러오기
img = cv2.imread('./dog.bmp')
cv2.imshow('image', img)

while True:
    keyvalue = cv2.waitKey()
    # i키를 누르면 이미지 반전
    if keyvalue == ord('i') or keyvalue == ord('I'):
        img = ~img
        cv2.imshow('image',img)
    elif keyvalue == 27: # ESC
        break
