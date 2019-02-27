import numpy as np
import cv2, sys


print("X:")
X=int(input())
print("Y")
Y=int(input())
print("Nombre del archivo: ")
N=input()+".png"

A = np.zeros((int(X),int(Y)),np.uint8)

cv2.line(A,(0,0),(511,200),(255,255,0),5)

cv2.circle(A,(447,63), 63, (0,0,255), 10)
cv2.circle(A,(200,200), 80, (255,0,255), -1)

cv2.circle(A, (200, 400), 100, (255,255,0), 2)

pts = np.array([[10,5], [20,30], [70,20], [50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(A, [pts], True, (255,255,0))

points = np.array([[123, 421], [206, 391], [1, 488], [458, 485]])
cv2.polylines(A, np.int32([points]), 10, (255,255,255))

r = cv2.imshow('image', A)
cv2.imwrite(N,A)

cv2.waitKey (0)
cv2.destroyAllWindows ()