import sys, numpy as np, cv2
from matplotlib import pyplot as plt
from array import array

Nombre = "p3_ensanchado.png" #input("Introduzca el nombre de la imagen con la extensión: ")
img = cv2.imread(Nombre, cv2.IMREAD_GRAYSCALE)
r = cv2.imshow(Nombre, img)
filas, columnas = img.shape

umbral = 127
result = np.zeros((filas, columnas), np.uint8)

for x in range(filas):
	for y in range(columnas):
		if img[x,y] > umbral:
			result[x,y] = 255
		else:
			result[x,y] = 0




p = cv2.imshow(Nombre+"umbralizacion", result)

cv2.imwrite("p3_umbralizacion.png",result)