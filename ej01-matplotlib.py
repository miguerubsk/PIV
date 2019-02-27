import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('triangulo.jpg', )
#cv2.imshow('triangulo.jpg', img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

#for row in hist:
#    for elem in row:
#        print(elem, end=' ')
#    print()

plt.plot(hist, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()