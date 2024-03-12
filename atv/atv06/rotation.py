import cv2 as cv
import numpy as np

rotation_point = None

def click_event(event, x, y, flags, param):
    global rotation_point
    if event == cv.EVENT_LBUTTONDOWN:
        rotation_point = (x, y)

img = cv.imread('atv/atv06/img/color_red.jpg')

cv.imshow('Image', img)
cv.setMouseCallback('Image', click_event)

while True:
    key = cv.waitKey(1) & 0xFF
    if key == ord('r') and rotation_point is not None:
        rows, cols = img.shape[:2]
        M = cv.getRotationMatrix2D(rotation_point, 90, 1)
        img = cv.warpAffine(img, M, (cols, rows))

        cv.imshow('Image', img)
    elif key == ord('q'):
        break

cv.destroyAllWindows()