import os
import cv2
import numpy as np

image = cv2.imread(os.path.join("images", "qrcode.jpg"))
cv2.imshow("image", image)
qrDecoder = cv2.QRCodeDetector()

data, bbox, rectifiedImage = qrDecoder.detectAndDecode(image)

print(data)

rectifiedImage = np.uint8(rectifiedImage)
cv2.imshow("rectifiedImage", rectifiedImage)

cv2.waitKey()
