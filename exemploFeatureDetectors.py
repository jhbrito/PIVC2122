from email.mime import image

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

sift = cv2.SIFT_create()
sift_kp, sift_desc = sift.detectAndCompute(imagem, None)
imagem_sift = imagem.copy()
imagem_sift = cv2.drawKeypoints(imagem_gray, sift_kp, None)
cv2.imshow("imagem_sift", imagem_sift)

# surf = cv2.xfeatures2d.SURF_create(400)
# surf_kp, surf_desc = surf.detectAndCompute(imagem, None)
# imagem_surf = imagem.copy()
# imagem_surf = cv2.drawKeypoints(imagem_gray, surf_kp, None)
# cv2.imshow("imagem_surf", imagem_surf)

orb = cv2.ORB_create()
orb_kp, orb_desc = orb.detectAndCompute(imagem, None)
imagem_orb = imagem.copy()
imagem_orb = cv2.drawKeypoints(imagem_gray, orb_kp, None)
cv2.imshow("imagem_orb", imagem_orb)

cv2.waitKey(0)
