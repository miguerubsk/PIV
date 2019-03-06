import sys, numpy as np, cv2
from matplotlib import pyplot as plt
from array import array


Nombre = "p3.png" #input("Introduzca el nombre de la imagen con la extensión: ")
img = cv2.imread(Nombre, cv2.IMREAD_GRAYSCALE)
filas, columnas = img.shape
r = cv2.imshow(Nombre, img)

conv = [[-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0]]

filt = np.zeros((filas, columnas), np.uint8)

img2 = np.zeros((filas+2, columnas+2), np.uint8)

for x in range(filas):
	for y in range(columnas):
		img2[x+1,y+1] = img[x,y]

for x in range(filas+2):
	for y in range(columnas+2):
		suma = 0
		if x<filas and y<columnas:
			for i in range(len(conv)):
				for j in range(len(conv)):
					suma+=img2[x+i,y+j]*conv[i][j]
				filt[x,y] = suma

p = cv2.imshow(Nombre+"conv", filt)
cv2.imwrite("p3_convolucion.png",filt)


cv2.waitKey (0)
cv2.destroyAllWindows ()