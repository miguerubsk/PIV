import sys, numpy as np, cv2, os
from matplotlib import pyplot as plt
from array import array
from time import time


def pintarVectores(flujo, img, espacio):
	espacio = int(espacio)
	filas, columnas, bandas = img.shape
	for i in range(0,filas, espacio):
		for j in range(0,columnas, espacio):
			cv2.circle(img,(j,i), 2, (0,0,255), -1)
			cv2.line(img,(j,i),(j+int(flujo[i,j][1]),i+int(flujo[i,j][0])),(0,255,0),1)




if __name__ == '__main__':
	os.system('clear')


	Nombre1 = input("Introduzca el nombre de la primera imagen con extension: ")
	imgGris1 = cv2.imread(Nombre1, cv2.IMREAD_GRAYSCALE)
	img1 = cv2.imread(Nombre1)
	Nombre2 = input("Introduzca el nombre de la segunda imagen con extension: ")
	imgGris2 = cv2.imread(Nombre2, cv2.IMREAD_GRAYSCALE)
	espacio = input("Introduzca el espaciado entre puntos: ")

	flujo = cv2.calcOpticalFlowFarneback(imgGris1, imgGris2, None, 0.5, 3, 15, 3, 5, 1.2, 0)

	pintarVectores(flujo, img1, espacio)
	x = Nombre1.split(".")

	cv2.imshow(x[0]+"_vectores",img1)
	cv2.imwrite(x[0]+"_"+espacio+"_result.png", img1)

	cv2.waitKey(0)
	os.system('clear')
	cv2.destroyAllWindows()