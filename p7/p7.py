import sys, numpy as np, cv2, os
from matplotlib import pyplot as plt
from array import array
from time import time



def pintarRectangulo(img, obj, r, g, b):

	for cuadrado in obj:
		x = cuadrado[0]
		y = cuadrado[1]
		w = cuadrado[2]
		h = cuadrado[3]
		cv2.rectangle(img,(x,y),(x+w,y+h),(b, g, r),3)
	return img



if __name__ == '__main__':
	os.system('clear')
	detectorCaras = cv2.CascadeClassifier("face.xml")
	detectorBocas = cv2.CascadeClassifier("mouth.xml")
	detectorOjos = cv2.CascadeClassifier("eye.xml")
	detectorNariz = cv2.CascadeClassifier("nose.xml")


	Nombre = input("Introduzca el nombre de la imagen con extension: ")
	imgGris = cv2.imread(Nombre, cv2.IMREAD_GRAYSCALE)
	img = cv2.imread(Nombre)


	caras = detectorCaras.detectMultiScale(imgGris, 1.3, 5)
	bocas = detectorBocas.detectMultiScale(imgGris, 1.8, 5)
	ojos  = detectorOjos.detectMultiScale(imgGris, 1.1, 20)
	nariz = detectorNariz.detectMultiScale(imgGris, 1.2, 5)



	img = pintarRectangulo(img, caras, 0, 0, 255 )
	img = pintarRectangulo(img, bocas, 255, 255, 0)
	img = pintarRectangulo(img, ojos, 0,255,0 )
	img = pintarRectangulo(img, nariz, 255, 0, 0 )


	cv2.imshow(Nombre+"_caras_sonrisas",img)
	cv2.imwrite("result.png", img)

	cv2.waitKey(0)
	os.system('clear')
	cv2.destroyAllWindows()