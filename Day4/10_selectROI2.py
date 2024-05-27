import cv2

isDrag = False
oldx = oldy = w = h = 0
color = (255,0,0)
img_copy = None

def on_mouse(event, x, y, flags, param):
    glabal oldx, oldy, w, h , isDrag, img_copy
    if event == cv2.EVENT_LBUTTONDOWN:
        pass # 과제
    elif event == cv2.EVENT_MOUSEMOVE:
        pass
    elif event == cv2.EVENT_LBUTTONUP:
        pass



img = cv2.imread('./sun.jpg')
cv2.imshow('img',img)
# cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()

# 이벤트 발생하면