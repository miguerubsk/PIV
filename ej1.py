import numpy as np
import cv2 , sys

img = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)

grises=[0 for i in range(255)]
for i in img:
    for j in i:
        grises[j]+=1
img2 = np.zeros((500, 256*3, 3), np.uint8)
img2[:]=(255 , 255, 255 )
x=0
for i in grises:
    cv2.rectangle(img2,(x,int((max(grises)-i)/40)),(x+3,int(max(grises)/40)),(0,0,0),-1)
    x+=3

r= cv2.imshow ('image ', img2 )
cv2.waitKey(0)
cv2.destroyAllWindows()