import cv2

woman = cv2.VideoCapture('./woman.mp4') # 1280 720
ham = cv2.VideoCapture('./ham.mp4')

hsv = cv2.cvtColor(woman, cv2.COLOR_BGR2HSV)
msk = cv2.inRange(hsv, (50,150,0), (80,255,255))

cv2.copyTo(woman, msk, ham)

cv2.imshow('woman',woman)

cv2.waitKey()
'''
width = int(woman.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(woman.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)
'''
