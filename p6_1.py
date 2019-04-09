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


def prob(img):
	grises=calculoHistograma(img)
	filas, columnas = img.shape
	x=0
	prob=[0 for i in range(256)]
	for i in grises:
		t=i/(filas*columnas)
		prob[x]=t
		x+=1
	return prob


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

def calcularUmbralOtsu(img):
	ecualizada = prob(img)

	mg = 0.0
	for i in range(256):
		mg = mg + i*ecualizada[i]

	mk = [0.0 for i in range(256)]
	pk = [0.0 for i in range(256)]

	#print(pk)
	for i in range(256):
		a=0.0
		b=0.0
		for j in range(i+1):
			a = a + j*ecualizada[j]
			b = b + ecualizada[j]
		mk[i] = a
		pk[i] = b
		
	#print(pk)
	maximo = 0.0
	
	nozzero = [0.0 for i in range(256)]
	#print(nozzero)
	resultado = [0.0 for i in range(256)]
	for k in range(256):
		nozzero[k] = 0.0
		#print(nozzero[k])
		a = pk[k]
		b = 1-pk[k]
		nozzero[k] = a*abs(b)
		#print(nozzero[k])
		
		if nozzero[k] != 0:
			resultado[k] = ((abs((mg * float(pk[k])) - float(mk[k]))**2)/nozzero[k])

	indice = 0
	for k in range(256):
		if resultado[k] > maximo:
			maximo = resultado[k]
			indice = k

	print("El umbral otsu es: "+str(indice))
	return indice



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



def umbralizarBloques(img, m, n, umbral):
	filas, columnas = img.shape
	x = int(filas/m)
	y = int(columnas/n)


	bloques = []
	for i in range(m):
		for j in range(n):
			bloque=np.zeros((x,y), np.uint8)
			for k in range(x):
				for l in range(y):
					bloque[k,l]=img[(i*x)+k,(j*y)+l]
		if umbral == "Otsu":
			bloque = umbralizar(bloque, calcularUmbralOtsu(bloque))
		if umbral == "General":
			bloque = umbralizar(bloque, calcularUmbralGeneral(bloque))

		bloques.append(bloque)

	ordenada = np.zeros((filas, columnas), np.uint8)
	l = 0
	o = 0
	for i in bloques:
		for j in range(x):
			for k in range(y):
				ordenada[(l*x)+j,(o*y)+k] = i[j,k]
		if l<n:
			l+=1
		if l==n:
			o+=1
			j=0
		#cv2.imshow("Ventana",ordenada)
		#cv2.waitKey (0)
	return ordenada








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
			result = umbralizar(img, calcularUmbralOtsu(img))
			#Se muestra la imagen resultante y se graba en un fichero
			#p = cv2.imshow(Nombre+"_umbralizacion_otsu", result)
			cv2.imwrite(Nombre+"_umbralizacion_otsu.png",result)
			print("Terminado, comprueba la imagen resultante:"+Nombre+" _umbralizacion_otsu.png")
			input("Pulsa una tecla para continuar")
			cv2.destroyAllWindows()
		elif opcionMenu=="3":
			Nombre = input("Introduzca el nombre de la imagen con extension: ")
			img = cv2.imread(Nombre, cv2.IMREAD_GRAYSCALE)
			Nombre = input("Introduce el nombre de la imagen a grabar: ")
			m = input("Introduzca el numero de divisiones en filas: ")
			n = input("Introduzca el numero de divisiones en columnas: ")
			umbral = input("Introduzca el tipo de umbral que desea usar (Otsu)(General): ")
			#Se mustra la imagen original
			#r = cv2.imshow(Nombre, img)
			#Se umbraliza la imagen con el método Otsu
			print("Umbralizando la imagen... \nEspera")
			cv2.imwrite(Nombre,umbralizarBloques(img, int(m), int(n), umbral))
			print("Terminado, comprueba la imagen resultante:"+Nombre)
			input("Pulsa una tecla para continuar")
			cv2.destroyAllWindows()
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