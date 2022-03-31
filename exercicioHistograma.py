# import cv2
from cv2 import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("images/cao.jpg", 0)
cv2.imshow("original", img)

fig = plt.figure(1)
# histograma = np.zeros(256, dtype=np.int)
# for y in range(img.shape[0]):
#     for x in range(img.shape[1]):
#         pix = img[y, x]
#         histograma[pix] = histograma[pix] + 1
#
# fig.add_subplot(2, 2, 1)
# plt.plot(histograma)
# plt.xlim([0, 255])
# plt.ylim([0, 15000])

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
fig.add_subplot(2, 3, 1)
plt.plot(hist)
plt.xlim([0, 255])
plt.ylim([0, 15000])

hist_norm = hist / (img.shape[0] * img.shape[1])
fig.add_subplot(2, 3, 2)
plt.plot(hist_norm)
plt.xlim([0, 255])

cdf = np.zeros(256)
cdf[0] = hist_norm[0]
for i in range(1, 256, 1):
    cdf[i] = cdf[i-1]+hist_norm[i]
fig.add_subplot(2, 3, 3)
plt.plot(cdf)
plt.xlim([0, 255])

img_eq = np.zeros(img.shape, dtype=np.uint8)
cdfmin = cdf[0]
for y in range(img_eq.shape[0]):
    for x in range(img_eq.shape[1]):
        img_eq[y, x] = int(np.round(((cdf[img[y, x]] - cdfmin) / (1 - cdfmin)) * (256 - 1)))

cv2.imshow("Equalized", img_eq)

hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])
fig.add_subplot(2, 3, 4)
plt.plot(hist_eq)
plt.xlim([0, 255])
plt.ylim([0, 15000])

hist_norm_eq = hist_eq / (img_eq.shape[0] * img_eq.shape[1])
fig.add_subplot(2, 3, 5)
plt.plot(hist_norm_eq)
plt.xlim([0, 255])

cdf_eq = np.zeros(256)
cdf_eq[0] = hist_norm_eq[0]
for i in range(1, 256, 1):
    cdf_eq[i] = cdf_eq[i-1]+hist_norm_eq[i]
fig.add_subplot(2, 3, 6)
plt.plot(cdf_eq)
plt.xlim([0, 255])

plt.show()
cv2.waitKey(0)
