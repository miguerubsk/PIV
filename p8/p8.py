import sys, numpy as np, cv2, os
from matplotlib import pyplot as plt
from array import array
from time import time


def pintarVectores(flujo, img):
	for i in flujo:
		for j in i:
			i+=8
			j+=8
			aux=flujo[i,j]
			img = cv2.circle(img,aux[0], 100, (0,0,255), -1)




if __name__ == '__main__':
	os.system('clear')


	Nombre1 = "foto1" #input("Introduzca el nombre de la imagen con extension: ")
	imgGris1 = cv2.imread(Nombre1+".jpg", cv2.IMREAD_GRAYSCALE)
	img1 = cv2.imread(Nombre1+".jpg")
	Nombre2 = "foto2" #input("Introduzca el nombre de la imagen con extension: ")
	imgGris2 = cv2.imread(Nombre2+".jpg", cv2.IMREAD_GRAYSCALE)
	img2 = cv2.imread(Nombre1+".jpg")

	flujo = cv2.calcOpticalFlowFarneback(imgGris1, imgGris2, None, 0.5, 3, 15, 3, 5, 1.2, 0)

	pintarVectores(flujo, img1)

	cv2.imshow(Nombre1+"vectores",img)

	cv2.waitKey(0)
	os.system('clear')
	cv2.destroyAllWindows()