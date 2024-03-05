import cv2 as cv
import numpy as np

# Carregar a imagem
img = cv.imread("atv/atv01/img/color_red.jpg")

hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# limtes da cor vermelha
minRed1 = np.array([0, 70, 50])
maxRed1 = np.array([10, 255, 255])
minRed2 = np.array([170, 70, 50])
maxRed2 = np.array([180, 255, 255])

# criando a mascara e combinando elas
mask1 = cv.inRange(hsvImg, minRed1, maxRed1)
mask2 = cv.inRange(hsvImg, minRed2, maxRed2)
matchMask = cv.bitwise_or(mask1, mask2)

result = cv.bitwise_and(img, img, mask=matchMask)

inverseMask = cv.bitwise_not(matchMask)

# aplicando cinza na imagem
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgGray = cv.cvtColor(imgGray, cv.COLOR_GRAY2BGR)

# resultado final depois de aplicar o cinza
resultImg = cv.bitwise_and(imgGray, imgGray, mask=inverseMask)
resultImg = cv.add(resultImg, result)

# exibindo as imagens
cv.imshow('img', img)
cv.imshow('result', result)
cv.imshow('inverseMask', inverseMask)
cv.imshow('resultImg', resultImg)
cv.waitKey(0)
cv.destroyAllWindows()