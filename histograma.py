import sys, numpy as np, cv2
from matplotlib import pyplot as plt
from array import array


Nombre = "triangulo.jpg" #input("Nombre de la imagen con la extensión: ")

img=cv2.imread(Nombre,cv2.IMREAD_GRAYSCALE)

r = cv2.imshow(Nombre, img)

filas, columnas = img.shape


histograma = [0 for i in range (256)]

for i in range(filas):
    for x in range(columnas):
        aux = img[i, x]
        histograma[aux] += 1


hist = np.zeros((500,256*3),np.uint8)
hist [hist == 0] = 255

max_altura = np.max(hist)
for x in range(256):
	altura = (histograma[x]/max_altura)*filas
	x1 = int(x*3)
	y1 = int(500-altura)
	x2 = int(x1+3)
	y2 = int(500)
	cv2.rectangle(hist, (x1,y1), (x2, y2), 0, -1)

t = cv2.imshow("histograma", hist)


plt.plot(histograma, color='gray' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

min = 0
max = 255
MAX = 0
MIN = 0

for m in range(filas):
	for n in range(columnas):
		if MAX < img[m,n]:
			MAX = img[m,n]
		if MIN > img[m,n]:
			MIN = img[m,n]

ensanchar = np.zeros((columnas,columnas),np.uint8)

for i in range(filas):
	for x in range(columnas):
		ensanchar[i,x] = min + ( ( (img[i,x]-MIN) - (MAX-MIN) ) / (MAX - MIN) )
 

#tuputamadre = cv2.imshow("NUEVA", ensanchar)

cv2.imwrite(Nombre+"-ensancahada.png",ensanchar)


cv2.waitKey (0)
cv2.destroyAllWindows ()