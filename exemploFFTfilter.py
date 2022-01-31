import cv2
import numpy as np
import os

image = cv2.imread(os.path.join("images", "baboon.png"))
cv2.imshow("image", image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_image)

I = gray_image/255.0
cv2.imshow("I", I)

I_fft = np.fft.fft2(I)
I_fft_v = np.abs(I_fft) / np.mean(np.mean(np.abs(I_fft)))
cv2.imshow("I_fft_v", I_fft_v)

I_fft_shift = np.fft.fftshift(I_fft)
I_fft_shift_v = np.abs(I_fft_shift) / np.mean(np.mean(np.abs(I_fft_shift)))
cv2.imshow("I_fft_shift_v", I_fft_shift_v)

tamanho = I_fft_shift.shape
H_lowpass = np.zeros(I_fft_shift.shape)
raio_maximo = tamanho[0]/2
raio = 0.25 * raio_maximo
centro_x = tamanho[1]/2
centro_y = tamanho[0]/2

for y in range(tamanho[0]):
    for x in range(tamanho[1]):
        d = np.sqrt((x-centro_x) ** 2 + (y-centro_y) ** 2)
        if d < raio:
            H_lowpass[y, x] = 0
        else:
            H_lowpass[y, x] = 1
cv2.imshow("H_lowpass", H_lowpass)

I_fft_shift_filtered = I_fft_shift * H_lowpass
I_fft_shift_filtered_v = np.abs(I_fft_shift_filtered) / np.mean(np.mean(np.abs(I_fft_shift_filtered)))
cv2.imshow("I_fft_shift_filtered_v", I_fft_shift_filtered_v)

I_fft_shift_filtered_unshift = np.fft.ifftshift(I_fft_shift_filtered)
I_fft_shift_filtered_unshift_v = np.abs(I_fft_shift_filtered_unshift) / np.mean(np.mean(np.abs(I_fft_shift_filtered_unshift)))
cv2.imshow("I_fft_shift_filtered_unshift_v", I_fft_shift_filtered_unshift_v)

I_fft_shift_filtered_unshift_ifft = np.fft.ifft2(I_fft_shift_filtered_unshift)
I_fft_shift_filtered_unshift_ifft = np.abs(I_fft_shift_filtered_unshift_ifft)

cv2.imshow("I_fft_shift_filtered_unshift_ifft", I_fft_shift_filtered_unshift_ifft)


cv2.waitKey()
