# ▪Implemente um programa que realize o ajuste de
# brilho (teclas 'a' e 'z'), ajuste de contraste (teclas 's' e 'x') 
# e aplique o efeito negativo (tecla 'n')

import cv2 as cv
import numpy as np

img = cv.imread("atv/atv01/img/color_red.jpg")

# os valores de contraste e brilho
alpha = 1.0 
beta = 0

while True:
    # ajustar o contraste e o brilho
    ajust_img = cv.convertScaleAbs(img, alpha=alpha, beta=beta)

    # Mostrar a imagem modificada
    cv.imshow('Adjusted Image', ajust_img)

    key = cv.waitKey(1) & 0xFF

    # ajustando o brilho e contraste
    if key == ord('q'):
        break
    elif key == ord('a'):
        beta = min(100, beta + 10)
    elif key == ord('z'):
        beta = max(-50, beta - 10)
    elif key == ord('s'):
        alpha = min(5.0, alpha + 0.1)
    elif key == ord('x'):
        alpha = max(0.1, alpha - 0.1)
    elif key == ord('n'):
        ajust_img = 255 - ajust_img
        cv.imshow('Negative Image', ajust_img)

cv.destroyAllWindows()