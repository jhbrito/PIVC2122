import cv2
import numpy as np

imagem = cv2.imread("PET-Body-02.jpg")
imagemFloat = np.array(imagem, dtype=np.float32)
imagemFloat = imagemFloat / 255.0
cv2.imshow("Original", imagemFloat)
cv2.waitKey(0)

imagemHSV = imagemFloat
# imagemHSV[:,:,0] = imagemFloat[:,:,0]*120+240
imagemHSV[:,:,0] = imagemFloat[:,:,0]*240+120
imagemHSV[:,:,1] = 1.0
imagemHSV[:,:,2] = 1.0
# imagemHSV[:,:,2] = imagemFloat[:,:,0]

imagemHSVBGR = cv2.cvtColor(imagemHSV, cv2.COLOR_HSV2BGR)
cv2.imshow("Final", imagemHSVBGR)
cv2.waitKey(0)

