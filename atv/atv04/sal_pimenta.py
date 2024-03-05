# Aplique um efeito de ruído do tipo sal e pimenta em
# um arquivo de vídeo ou imagem da webcam, variando
# sua intensidade por comandos de teclado.

import cv2
import numpy as np
import random

# função de ruído sal e pimenta
def noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

# abir webcam
cap = cv2.VideoCapture(0)

qtd_ruido = 0.05

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # adicionar ruído
    frame_with_noise = noise(frame, qtd_ruido)

    # mostrar ruído
    cv2.imshow('Sal e Pimenta', frame_with_noise)

    key = cv2.waitKey(1) & 0xFF

    # ajustar o valor do ruído
    if key == ord('q'):
        break
    elif key == ord('a'):
        qtd_ruido = min(1, qtd_ruido + 0.05)
    elif key == ord('z'):
        qtd_ruido = max(0, qtd_ruido - 0.05)

cap.release()
cv2.destroyAllWindows()