#edge detection

import cv2
import numpy as np

img = cv2.imread('/Users/sathvik/work/python/RetinaDiag/imgs/src/RetinalScan/im0001.ppm', cv2.IMREAD_GRAYSCALE)
cv2.imshow("original", img)
rows, cols = img.shape

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('Original', img)
cv2.imshow('Sobel horizontal', sobel_horizontal)
cv2.imshow('Sobel vertical', sobel_vertical)

cv2.waitKey(0)
