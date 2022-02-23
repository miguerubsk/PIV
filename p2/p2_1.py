import sys, numpy as np, cv2



Nombre = input("Introduzca el nombre de la imagen con la extensión: ")

A = cv2.imread(Nombre)

if ( A.all() ):
	print (" Error al cargar imagen ")
	sys . exit ()


filas, columnas, bandas = A.shape

B = np.zeros((columnas, filas, bandas),np.uint8)
f=0

for i in range(filas):
    c = 0
    f -= 1

    for x in range(columnas):
        B[c,f] = A[i,x]
        c+=1

r = cv2.imshow('image', B)
cv2.imwrite(Nombre+"-rotada.png",B)

cv2.waitKey (0)
cv2.destroyAllWindows ()