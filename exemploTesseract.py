import cv2
import pytesseract

tesseract_path = "C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_path

img = cv2.imread("images/texto.jpg")
cv2.imshow("img", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_gray", img_gray)

ret, thresh1 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
cv2.imshow("thresh1", thresh1)

texto = pytesseract.image_to_string(thresh1)
print(texto)

cv2.waitKey()
