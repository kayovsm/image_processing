import cv2
import numpy as np

img = cv2.imread('atv\img\cars.png')

# 1384 x 579
# pontos da imagem que materam o foco 
points = np.array([[1100,10], [700,10], [700,480], [1100,480]])

# mascara com o mesmo tamanho da imagem
mask = np.zeros(img.shape, dtype=np.uint8)

# colocar branco no desenho formado pelos pontos
cv2.fillPoly(mask, [points], (255,255,255))

# desfoque gaussiano
blurred = cv2.GaussianBlur(img, (29, 29), 0)

output = np.where(mask==np.array([255, 255, 255]), img, blurred)

cv2.imshow('Resultado', output)
cv2.waitKey(0)
cv2.destroyAllWindows()