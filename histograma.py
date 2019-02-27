import sys, numpy as np, cv2
from matplotlib import pyplot as plt
from array import array


Nombre = input("Nombre de la imagen con la extensión: ")

img=cv2.imread(Nombre,cv2.IMREAD_GRAYSCALE)

r = cv2.imshow(Nombre, img)

filas, columnas = img.shape

histograma=[0 for i in range(256)]
for i in img:
    for j in i:
        histograma[j]+=1
hist = np.zeros((500, 256*3, 3), np.uint8)
hist[:]=(255 , 255, 255 )
x=0
for i in histograma:
    cv2.rectangle(hist,(x,int((max(histograma)-i)/40)),(x+3,int(max(histograma)/40)),(0,0,0),-1)
    x+=3

r= cv2.imshow ('image ', hist )


#plt.plot(histograma, color='gray' )
#plt.xlabel('intensidad de iluminacion')
#plt.ylabel('cantidad de pixeles')
#plt.show()

xmax = 0
xmin = 0

for m in range(256):
	if histograma[m] != 0: 
		xmin = m 
		break

for n in reversed(range(256)):
	if histograma[n] != 0: 
		xmax = n
		break
		

print("Valor máximo: " + str(xmax))
print("Valor mínimo: " + str(xmin))

ensanchar = np.zeros((filas,columnas),np.uint8)

for i in range(filas):
	for x in range(columnas):
		ensanchar[i,x] = 0 + ( ( (img[i,x]-xmin) * 255 ) / (xmax - xmin) )
 

g = cv2.imshow("CONTRASTE", ensanchar)

cv2.imwrite("p3_ensanchado.png",ensanchar)


cv2.waitKey (0)
cv2.destroyAllWindows ()