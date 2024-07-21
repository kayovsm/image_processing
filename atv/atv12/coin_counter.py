import numpy as np
import cv2
from matplotlib import pyplot as plt

# img = cv2.imread("atv/img/coin_three.jpg")
img = cv2.imread("atv/img/coin_five.png")
img = cv2.resize(img, (352, 475))

image_copy = img.copy()

# aplicando gaussiano
img_blur = cv2.GaussianBlur(img, (7, 7), 3)

# convertendo para escala de cinza
gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

# aplicando threshold
ret, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)

# pegando os contornos das moedas
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# calculando a area dos contornos de cada moeda
area = {}
for i in range(len(contours)):
    cnt = contours[i]
    ar = cv2.contourArea(cnt)
    area[i] = ar

# ordenando as moedas pela area dos contornos
srt = sorted(area.items(), key=lambda x: x[1], reverse=True)
results = np.array(srt).astype("int")

# filtrando as moedas por area
num = np.argwhere(results[:, 1] > 500).shape[0]

# desenhando os contornos das moedas na imagem original
for i in range(1, num):
    image_copy = cv2.drawContours(image_copy, contours, results[i, 0], (0, 255, 0), 3)

print("NUMERO DE MOEDAS", num - 1)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_blur_rgb = cv2.cvtColor(img_blur, cv2.COLOR_BGR2RGB)
gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
thresh_rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
image_copy_rgb = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

fig, axs = plt.subplots(1, 5, figsize=(20, 10))
axs[0].imshow(img_rgb)
axs[0].set_title('ORIGINAL')
axs[1].imshow(img_blur_rgb)
axs[1].set_title('BLUR')
axs[2].imshow(gray_rgb)
axs[2].set_title('GRAY')
axs[3].imshow(thresh_rgb)
axs[3].set_title('THRESHOLD')
axs[4].imshow(image_copy_rgb)
axs[4].set_title('RESULTADO: ' + str(num - 1) + ' MOEDAS')

plt.show()