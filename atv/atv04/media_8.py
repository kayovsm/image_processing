# Faça a redução da resolução de uma imagem tomando
# por base a média dos pixels na vizinhança-8.

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
resized_img = cv.resize(img, (new_width, new_height), interpolation = cv.INTER_AREA)

# salvando a nova imagem
cv.imwrite("media8_img.jpg", resized_img)