from cv2 import cv2 as cv2
import numpy as np
import os

# load da imagem
folder = "images"
img = cv2.imread(os.path.join(folder, "moedas.jpg"), cv2.IMREAD_GRAYSCALE)
print(img.shape)
cv2.namedWindow("Moedas")
cv2.imshow("Moedas", img)
# cv2.waitKey()

# threshold da imagem
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Moedas Thresh", th2)
print(th2.shape)
# cv2.waitKey()

# dilate
kernel = np.ones((3, 3), dtype=np.uint8)
dilate = cv2.dilate(th2, kernel)
cv2.imshow("Dilate", dilate)
print(dilate.shape)
# cv2.waitKey()

# erode
erode = cv2.erode(dilate, kernel)
cv2.imshow("Erode", erode)
print(erode.shape)
# cv2.waitKey()

# imagem segmentada = imagem original x mascara
mascara = np.uint8(erode / 255)
imagem_segmentada = img * (mascara)
cv2.imshow("imagem_segmentada", imagem_segmentada)
print(imagem_segmentada.shape)
cv2.waitKey()

#
