import numpy as np
import cv2

a = np.ndarray((704, 576), dtype=np.uint8)
a[0:, 0:] = 127
# a[0:] = 127
a[0:10, :] = 0
# a[-10:, :] = 0
s=a.shape
a[s[0]-10:s[0], :]=0

a[:, 0:10] = 0
# a[:, s[1]-10:s[1]] = 0
a[:, -10:] = 0

cv2.imshow("Imagem", a)
cv2.waitKey(0)
