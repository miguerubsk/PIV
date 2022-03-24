import cv2, sys

nombreImagen = "p4.png"


imagen = cv2.imread(nombreImagen, cv2.IMREAD_GRAYSCALE)

if (imagen is None):
    print("Error al cargar la imagen")
    sys.exit()

cv2.imshow('original', imagen)

"""Ecualizamos el histograma"""
ecualizada = cv2.equalizeHist(imagen)

cv2.imshow('resultado', ecualizada)


cv2.waitKey(0)
cv2.destroyAllWindows()