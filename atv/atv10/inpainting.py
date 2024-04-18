# coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import cv2

def inpaint(image, mask):
    # Converter a imagem para float para evitar overflow
    image = image.astype(float)

    # Obter a altura e a largura da imagem
    height, width = image.shape[:2]

    # Criar uma cópia da imagem para modificar
    output = image.copy()

    # Loop sobre cada pixel na máscara
    for y in range(height):
        for x in range(width):
            # Se o pixel atual está na máscara
            if mask[y, x] > 0:
                # Obter os pixels vizinhos
                neighbors = []
                if y > 0: neighbors.append(output[y-1, x])
                if y < height-1: neighbors.append(output[y+1, x])
                if x > 0: neighbors.append(output[y, x-1])
                if x < width-1: neighbors.append(output[y, x+1])

                # Substituir o pixel atual pela média dos vizinhos
                output[y, x] = np.mean(neighbors, axis=0)

    # Converter a imagem de volta para uint8
    output = output.astype(np.uint8)

    return output

# Carregar a imagem e a máscara
img = cv2.imread('atv/img/inpaint_opencv.png')
mask = cv2.imread('atv/img/inpaint_mask.png',0)

# Juntar a imagem e a máscara
# combined = cv2.bitwise_and(img, img, mask=mask)

# Remover a máscara da imagem combinada
inpaint = inpaint(img, mask)

# Mostrar as imagens
plt.subplot(221), plt.imshow(img)
plt.title('Imagem Original')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('Máscara')
# plt.subplot(223), plt.imshow(combined)
# plt.title('Imagem Combinada')
plt.subplot(224), plt.imshow(inpaint)
plt.title('Imagem sem Máscara')

plt.tight_layout()
plt.show()