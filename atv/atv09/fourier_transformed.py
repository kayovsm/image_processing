import cv2
import numpy as np
from matplotlib import pyplot as plt

#pegar as coordenadas dos pontos
def findCoordinates(spectrum, numPoints, minDistance, points):
    if points is None:
        points = []

    if len(points) >= numPoints:
        return points

    spectrumCopy = spectrum.copy()

    spectrumHeight, spectrumWidth = spectrum.shape
    centerRow, centerCol = spectrumHeight // 2, spectrumWidth // 2
    spectrumCopy[centerRow-30:centerRow+30, centerCol-30:centerCol+30] = 0

    maxIndex = np.argmax(spectrumCopy)
    point = np.unravel_index(maxIndex, spectrum.shape)[::-1]

    if all(np.linalg.norm(np.array(point) - np.array(existingPoint)) >= minDistance for existingPoint in points):
        points.append(point)

    spectrumCopy[point[1], point[0]] = 0

    return findCoordinates(spectrumCopy, numPoints, minDistance, points)

inputImage = cv2.imread('atv/img/clown.jpg',0)

fourierTransform = np.fft.fft2(inputImage)
shiftedFourier = np.fft.fftshift(fourierTransform)
magnitudeSpectrum = np.log(np.abs(shiftedFourier)) / 20

imgH, imgW = inputImage.shape
centerRow, centerCol = imgH//2 , imgW//2
lowPassMask = np.zeros((imgH,imgW),np.uint8)
lowPassMask[centerRow-60:centerRow+60, centerCol-60:centerCol+60] = 1

lowPassMask = np.ones_like(inputImage) * 255

coordinates = findCoordinates(magnitudeSpectrum, 4, 5, None)
print('Points: ', coordinates)
# points = [(562, 553), (561, 555), (561, 553), (561, 554)]

# desenhando o circulo de acordo com as coordenadas
for point in coordinates:
    cv2.circle(lowPassMask, point, radius=18, color=0, thickness=-1)

blurredMask = cv2.GaussianBlur(lowPassMask, (29, 29), 0)

# aplicando a máscara na transformada de fourier
maskedFourier = np.multiply(shiftedFourier, blurredMask) / 255
inverseShiftedFourier = np.fft.ifftshift(maskedFourier)
inverseFourierImage = np.fft.ifft2(inverseShiftedFourier)
inverseFourierImage = np.abs(inverseFourierImage)

(fig, ax) = plt.subplots(1, 3, figsize=(12, 5))
ax[0].imshow(inputImage, cmap="gray")
ax[0].set_title("Original Image")
ax[0].set_xticks([])
ax[0].set_yticks([])

ax[1].imshow(magnitudeSpectrum, cmap="gray")
ax[1].set_title("Magnitude Spectrum")
ax[1].set_xticks([])
ax[1].set_yticks([])

ax[2].imshow(inverseFourierImage, cmap="gray")
ax[2].set_title("Filtered Image")
ax[2].set_xticks([])
ax[2].set_yticks([])

plt.show()