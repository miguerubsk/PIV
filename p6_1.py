import sys, numpy as np, cv2
from matplotlib import pyplot as plt
from array import array

def calculoHistograma(img):
	histograma=[0 for i in range(256)]
	for i in img:
	    for j in i:
	        histograma[j]+=1
	return histograma

def calcularUmbralGeneral(img):
	umbral = 127
	T = 0

	filas, columnas = img.shape
	while T != umbral:
		aux1 = 0
		aux2 = 0
		g1 = 0
		g2 = 0

		for i in range(filas):
			for j in range(columnas):
				if img[i,j] < umbral:
					g1+=1
					aux1 += img[i,j]
				else: 
					g2+=1
					aux2 += img[i,j]
		T = umbral
		umbral = ( (aux1/g1) + (aux2/g2) )/2
	
	print("El umbral es: "+str(umbral))

	return umbral

def calcularUmbralOtsu(histograma):
	#vector de probabilidad acumulada
	omega = [0 for i in range(256)]

	mean = [0 for i in range(256)]

	omega[0] = histograma[0]
	for i in range(len(histograma)):
		omega[i] = omega[i-1] + histograma[i]
		mean[i] = mean[i-1] + i*histograma[i]
	sigmab2 = 0
	mt = mean[len(histograma)-1]
	sigmab2max = 0
	T = 0
	for i in range(len(histograma)):
		clase1 = omega[i]
		clase2 = 1- clase1
		if clase1 != 0 and clase2 != 0:
			m1 = mean[i] / clase1
			m2 = (mt -mean[i]) / clase2
			sigmab2 = (clase1 * (m1 - mt) * (m1 - mt) +clase2 * (m2 - mt) * (m2 - mt))
			if sigmab2 > sigmab2max:
				sigmab2max = sigmab2
				T = i
				print(str(i))
	print("El umbral es: "+str(T))
	return int(T)



def umbralizar(img, umbral):

	filas, columnas = img.shape
	result = np.zeros((filas, columnas), np.uint8)

	for x in range(filas):
		for y in range(columnas):
			if img[x,y] > umbral:
				result[x,y] = 255
			else:
				result[x,y] = 0
	return result




if __name__ == '__main__':

	Nombre = "triangulo.png" #input("Introduzca el nombre de la imagen con extension: ")
	img = cv2.imread(Nombre, cv2.IMREAD_GRAYSCALE)
	r = cv2.imshow(Nombre, img)

	#result = umbralizar(img, calcularUmbralGeneral(img))
	#p = cv2.imshow(Nombre+"_umbralizacion", result)
	#cv2.imwrite("p3_umbralizacion.png",result)

	result = umbralizar(img, calcularUmbralOtsu(calculoHistograma(img)))
	p = cv2.imshow(Nombre+"_umbralizacion_otsu", result)
	cv2.imwrite("p3_umbralizacion_otsu.png",result)

	cv2.waitKey (0)
	cv2.destroyAllWindows()#