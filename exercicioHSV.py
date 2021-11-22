import cv2
import numpy as np

imagem = cv2.imread("cao.jpg")
imagemFloat = np.array(imagem, dtype=np.float32)
imagemFloat = imagemFloat / 255.0
cv2.imshow("Original", imagemFloat)
cv2.waitKey(0)

imagemHSV = cv2.cvtColor(imagemFloat, cv2.COLOR_BGR2HSV)

imagemHSV[:,:,0] = 360.0

imagemHSVBGR = cv2.cvtColor(imagemHSV, cv2.COLOR_HSV2BGR)
cv2.imshow("Final", imagemHSVBGR)
cv2.waitKey(0)


a=0

