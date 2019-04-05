import sys, numpy as np, cv2, os
from matplotlib import pyplot as plt
from array import array



def menu():
	os.system('clear')
	print("========================MENÚ========================")
	print("\t1 - Umbralización general")
	print("\t2 - Umbralización otsu")
	print("\t3 - Umbralización por bloques")
	print("\t4 - Umbralización por pixel")
	print("\t0 - salir")
	print("====================================================")


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
	
	print("El umbral general es: "+str(umbral))

	return umbral

def calcularUmbralOtsu(histograma):
	val_max = -999
	umbral = -1
	q1 = 0
	q2 = 0
	m1 = 0
	m2 = 0
	val = 0
	for t in range(1,255):
	    q1 = np.sum(histograma[:t])
	    q2 = np.sum(histograma[t:])
	    m1 = np.sum(np.array([i for i in range(t)])*histograma[:t])/q1
	    m2 = np.sum(np.array([i for i in range(t,256)])*histograma[t:])/q2
	    val = q1*(1-q1)*np.power(m1-m2,2)
	    if val_max < val:
	        val_max = val
	        umbral = t
	print("El umbral otsu es: " + str(umbral))
	return umbral



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



#def umbralizarBloques(img):





if __name__ == '__main__':

	while True:
		menu()
		opcionMenu = input("Elija una opción: ")
		if opcionMenu=="1":
			#Carga de la imagen con la que se va a trabjar
			Nombre = input("Introduzca el nombre de la imagen con extension: ")
			img = cv2.imread(Nombre, cv2.IMREAD_GRAYSCALE)
			#Se mustra la imagen original
			#r = cv2.imshow(Nombre, img)
			#Se umbraliza con el método general
			print("Umbralizando la imagen... \nEspera")
			result = umbralizar(img, calcularUmbralGeneral(img))
			#Se muestra la imagen resultante y se graba en un fichero
			#p = cv2.imshow(Nombre+"_umbralizacion", result)
			cv2.imwrite(Nombre+"_umbralizacion_general.png",result)
			print("Terminado, comprueba la imagen resultante: "+Nombre+"_umbralizacion_general.png")
			input("Pulsa una tecla para continuar")
			cv2.destroyAllWindows()
		elif opcionMenu=="2":
			#Carga de la imagen con la que se va a trabjar
			Nombre = input("Introduzca el nombre de la imagen con extension: ")
			img = cv2.imread(Nombre, cv2.IMREAD_GRAYSCALE)
			#Se mustra la imagen original
			#r = cv2.imshow(Nombre, img)
			#Se umbraliza la imagen con el método Otsu
			print("Umbralizando la imagen... \nEspera")
			result = umbralizar(img, calcularUmbralOtsu(calculoHistograma(img)))
			#Se muestra la imagen resultante y se graba en un fichero
			#p = cv2.imshow(Nombre+"_umbralizacion_otsu", result)
			cv2.imwrite(Nombre+"_umbralizacion_otsu.png",result)
			print("Terminado, comprueba la imagen resultante:"+Nombre+" _umbralizacion_otsu.png")
			input("Pulsa una tecla para continuar")
			cv2.destroyAllWindows()
		elif opcionMenu=="3":
			print("NO SOPORTADO")
			input("Pulsa una tecla para continuar")
		elif opcionMenu=="4":
			print("NO SOPORTADO")
			input("Pulsa una tecla para continuar")
		elif opcionMenu=="0":
			cv2.destroyAllWindows()
			os.system('clear')
			break
		else:
			print ("")
			input("No has pulsado ninguna opción correcta...\nPulsa una tecla para continuar")