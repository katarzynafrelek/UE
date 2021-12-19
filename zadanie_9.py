import cv2
import pytesseract as pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


""" obraz1"""
img = cv2.imread('obraz1.jpg')
img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))


""" obraz2"""
img = cv2.imread('obraz2.jpg')
img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))


""" obraz3"""
img = cv2.imread('obraz3.jpg')
img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))


""" obraz4"""
img = cv2.imread('obraz4.jpg')
img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))


""" obraz5"""
img = cv2.imread('obraz5.jpg')
img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))
