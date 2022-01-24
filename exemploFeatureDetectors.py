import cv2

imagem = cv2.imread("Sharbat_Gula.jpg")
cv2.imshow("Imagem", imagem)

imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem Gray", imagem_gray)

harris_corners = cv2.cornerHarris(imagem_gray, blockSize=2, ksize=3, k=0.04)
# cv2.imshow("harris_corners", harris_corners)
imagem_harris = imagem.copy()
imagem_harris[harris_corners > 0.01*harris_corners.max()] = [255, 0, 0]
cv2.imshow("imagem_harris", imagem_harris)

cv2.waitKey(0)
