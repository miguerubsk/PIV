import sys, numpy as np, cv2
from matplotlib import pyplot as plt
from array import array


Nombre = "p3.png" #input("Introduzca el nombre de la imagen con la extensión: ")
img = cv2.imread(Nombre, cv2.IMREAD_GRAYSCALE)
r = cv2.imshow(Nombre, img)


conv = [[-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0]]

kernel = np.asarray(conv)
dst = cv2.filter2D(img, -1, kernel)
print(dst.min(), dst.max())
norm = cv2.normalize(dst, None, 0, 255, cv2.NORM_MINMAX)
print(norm.min(), norm.max())

p = cv2.imshow(Nombre+"conv", norm)

cv2.waitKey (0)
cv2.destroyAllWindows ()