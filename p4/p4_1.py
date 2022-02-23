import cv2, sys
import numpy as np
from matplotlib import pyplot as plt

entrada = input("Nombre de la imagen: ")


img = cv2.imread(entrada, cv2.IMREAD_GRAYSCALE)
cv2.imshow('original',img)

"""Ecualizamos el histograma"""
ecualizada = cv2.equalizeHist(img)

cv2.imshow('resultado',ecualizada)


cv2.waitKey(0)
cv2.destroyAllWindows()