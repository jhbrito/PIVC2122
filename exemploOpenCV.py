import cv2

imagem = cv2.imread("cao.jpg")
imagem[200:300, 400:600, 0:1] = 0
imagem2 = imagem/255.0

cv2.imshow("Imagem", imagem)
cv2.imshow("Imagem2", imagem2)
cv2.waitKey(0)
