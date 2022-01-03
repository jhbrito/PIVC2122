import numpy as np
from cv2 import cv2 as cv2
import os

folder = "images"
img = cv2.imread(os.path.join(folder, "moedas.jpg"))
window_name = "Moedas"
cv2.namedWindow(window_name)
cv2.imshow("Moedas", img)


def on_trackbar_change(val):
    ret, img_threshold = cv2.threshold(img, val, 255, 0)
    cv2.imshow("Moedas threshold", img_threshold)


cv2.createTrackbar("threshold", window_name, 127, 255, on_trackbar_change)
on_trackbar_change(127)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("Otsu", img_otsu)

cv2.waitKey()
