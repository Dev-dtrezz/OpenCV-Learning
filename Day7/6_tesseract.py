import cv2
import pytesseract

img = cv2.imread('./hello.png')
# 색상변경 RGB_테서렉트에서는 RGB로 인식
dst = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# 이미지를 스트링으로_lang=kor(한국어)+eng(영어)
text = pytesseract.image_to_string(dst, lang='kor+eng')
print(text)
