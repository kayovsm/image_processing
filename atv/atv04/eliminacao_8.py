# Faça a redução da resolução de uma imagem tomando
# por base a eliminação dos pixels da vizinhança-8.

import cv2 as cv
import numpy as np

# Carregar a imagem
img = cv.imread("atv/atv04/img/color_red.jpg")

# dimensões da imagem
height, width = img.shape[:2]

# novas dimensões
new_width = width // 8
new_height = height // 8

# nova imagem 
resized_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)

# copiando o pixel da vizinhança-8
for i in range(new_height):
    for j in range(new_width):
        resized_img[i, j] = img[i*8, j*8]

# salvando a nova imagem
cv.imwrite("eliminacao8_img.jpg", resized_img)