import sys, numpy as np, cv2


Nombre = input("Introduzca el nombre de la imagen con la extensión: ")

A = cv2.imread(Nombre)

if ( A.all() ):
	print (" Error al cargar imagen ")
	sys . exit ()


filas, columnas, bandas = A.shape

B = np.zeros((filas, columnas, bandas),np.uint8)

for i in range(filas):

    for x in range(columnas):
        B[i,x] = A[i,-x]

r = cv2.imshow('image', B)
cv2.imwrite(Nombre+"-espejada.png",B)

cv2.waitKey (0)
cv2.destroyAllWindows ()