import sys, numpy as np, cv2



Nombre = input("Introduzca el nombre del video con la extensión: ")

cap = cv2.VideoCapture(Nombre)

while (cap.isOpened()):
	ret,frame = cap.read()
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame,"MIGUEL GONZALEZ GARCIA",(5,560), font, 3, (255,255,255),1)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	cv2.imshow("frame",gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows