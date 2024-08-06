# QUESTÃO 01

# RESPOSTAS: opening, dilatação e closing

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('avl02/img/Original.png', cv2.IMREAD_GRAYSCALE)

_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# encontrar bordas na imagem
edges = cv2.Canny(thresh, 100, 200)

# encontrar contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# desenhando os contornos
contours_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

circle_count = 0
square_count = 0

# Desenhar contornos coloridos conforme a forma geométrica
for contour in contours:
    # Aproximar o contorno para polígono
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

    # Desenhar contornos na imagem de contornos
    cv2.drawContours(contours_image, [approx], 0, (255, 0, 0), 2)

    # encontrando circulos
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    circularity = 4 * np.pi * (cv2.contourArea(contour) / (cv2.arcLength(contour, True) ** 2))
    
    if 0.85 < circularity < 1.15:
        print("Círculo detectado")
        cv2.circle(output, center, radius, (0, 0, 255), -1)
        circle_count += 1
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        if 0.9 <= aspect_ratio <= 1.1:
            print("Quadrado detectado")
            cv2.drawContours(output, [approx], 0, (0, 255, 0), -1)
            square_count += 1
    else:
        print("Outra forma detectada")
        cv2.drawContours(output, [approx], 0, (255, 0, 0), -1)

image_rgb = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
contours_image_rgb = cv2.cvtColor(contours_image, cv2.COLOR_BGR2RGB)
output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(contours_image_rgb)
axs[1].set_title('Contours')
axs[2].imshow(output_rgb)
axs[2].set_title('Painted Shapes')

for ax in axs:
    ax.axis('off')

plt.show()

print(f"Quantidade de círculos: {circle_count}")
print(f"Quantidade de quadrados: {square_count}")