import cv2 as cv2
import numpy as np
import os

folder = "images"
img = cv2.imread(os.path.join(folder, "moedas.jpg"))
window_name = "Moedas"
cv2.namedWindow(window_name)
cv2.imshow("Moedas", img)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


canny_thresh_min = 150
canny_thresh_max = 200
edges = cv2.Canny(gray_image, canny_thresh_min, canny_thresh_max)


def on_trackbar_canny_min(val):
    global canny_thresh_min, edges
    canny_thresh_min = val
    edges = cv2.Canny(gray_image, canny_thresh_min, canny_thresh_max)
    cv2.imshow("Moedas Canny", edges)


def on_trackbar_canny_max(val):
    global canny_thresh_max, edges
    canny_thresh_max = val
    edges = cv2.Canny(gray_image, canny_thresh_min, canny_thresh_max)
    cv2.imshow("Moedas Canny", edges)

cv2.namedWindow("Moedas Canny")
cv2.createTrackbar("canny_thresh_min", "Moedas Canny", canny_thresh_min, 1024, on_trackbar_canny_min)
cv2.createTrackbar("canny_thresh_max", "Moedas Canny", canny_thresh_max, 1024, on_trackbar_canny_max)
cv2.imshow("Moedas Canny", edges)


gray_image_float = gray_image/255.0

Mx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
My = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

dx = cv2.filter2D(gray_image_float, -1, kernel=Mx)
cv2.imshow("dx", dx)

dy = cv2.filter2D(gray_image_float, -1, kernel=My)
cv2.imshow("dy", dy)

gradient = np.sqrt(dx**2+dy**2)

# gradient = np.float32(gradient)
cv2.imshow("Gradiente", gradient)
cv2.waitKey()
#
# gradient = np.reshape(gradient, (246, 300, 1))

th = 200/300.0
ret, thresholded_gradient = cv2.threshold(gradient, th, 255, 0)

def on_trackbar_th(val):
    global th
    th = val/100.0
    ret, thresholded_gradient = cv2.threshold(gradient, th, 255, 0)
    cv2.imshow("Moedas Gradient", thresholded_gradient)


cv2.namedWindow("Moedas Gradient")
cv2.createTrackbar("th", "Moedas Gradient", int(th*300), 300, on_trackbar_th)
cv2.imshow("Moedas Gradient", thresholded_gradient)


cv2.waitKey()
