import numpy as np
from cv2 import cv2 as cv2

def convolucao(imagem, filtro):
    (H, W) = imagem.shape
    offset = (int)(np.floor(filtro.shape[0]/2))
    img_expandida = np.zeros((H+2*offset, W+2*offset))
    print(img_expandida.shape)
    img_expandida[1:img_expandida.shape[0]-1, 1:img_expandida.shape[1]-1] = imagem
    img_expandida[0, 1:img_expandida.shape[1]-1] = img_expandida[1, 1:img_expandida.shape[1]-1]
    img_expandida[-1, 1:img_expandida.shape[1]-1] = img_expandida[-2, 1:img_expandida.shape[1]-1]
    img_expandida[1:img_expandida.shape[0]-1, 0] = img_expandida[1:img_expandida.shape[0]-1, 1]
    img_expandida[1:img_expandida.shape[0]-1, -1] = img_expandida[1:img_expandida.shape[0]-1, -2]
    img_expandida[0, 0] = img_expandida[1,1]
    img_expandida[0, -1] = img_expandida[1, -2]
    img_expandida[-1, 0] = img_expandida[-2, 1]
    img_expandida[-1, -1] = img_expandida[-2, -2]
    resultado = np.zeros(imagem.shape)
    for y in range(resultado.shape[0]):
        for x in range(resultado.shape[1]):
            v = 0
            for ky in range(filtro.shape[0]):
                for kx in range(filtro.shape[1]):
                    kv = filtro[ky, kx]
                    pixel = img_expandida[y+ky, x+kx]
                    v = v + kv*pixel
            resultado[y, x] = v
    return resultado


img = cv2.imread("cao.jpg", 0)
img = img /255.0
cv2.imshow("original", img)

# filtro = np.ones((3, 3), dtype="float32")
filtro = [ [0, -1, 0],
           [-1, 4, -1],
           [0, -1, 0] ]
filtro = [ [1/9, 1/9, 1/9],
           [1/9, 1/9, 1/9],
           [1/9, 1/9, 1/9] ]
filtro = np.array(filtro)
imagem_filtrada2 = cv2.filter2D(img, -1, kernel=filtro)
cv2.imshow("resultado2", imagem_filtrada2)

imagem_filtrada = convolucao(img, filtro)
cv2.imshow("resultado", imagem_filtrada)
cv2.waitKey(0)
print("end")
