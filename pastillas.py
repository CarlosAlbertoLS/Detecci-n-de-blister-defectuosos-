#Importacion de la libreria cv2
import cv2

#Lectura de una imagen
img = cv2.imread('p13.jpg')

#Transformacion de la imagen en formato BGR aescala de grises
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Aplicacion de filtros de suavizado
median = cv2.medianBlur(imgray,25)
blur = cv2.GaussianBlur(median,(11,11),290)

#Aplicacion del filtro de umbralizacion simple
_,th = cv2.threshold(blur, 82, 255, cv2.THRESH_BINARY)

#Funcion para encontrar contornos
cnts,_ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Fuente para escribir el numero de contorno
font = cv2.FONT_HERSHEY_SIMPLEX
i=0

print('Contornos: ', len(cnts))

#Ciclo que permite iterar desde el primer hasta el ultimo contorno y dibujarlos 
for c in cnts:
	M = cv2.moments(c)
	if(M["m00"] == 0): M["m00"] = 1
	x=int(M["m10"]/M["m00"])
	y=int(M['m01']/M['m00'])

	mensaje = 'Num: ' + str(i+1)
	cv2.putText(img, mensaje, (x-40,y),font,0.75,
		(255,0,0),2,cv2.LINE_AA)
	cv2.drawContours(img, [c], 0, (255,0,0),2)
	cv2.imshow("Conteo contornos", img)
	cv2.waitKey(0)
	i=i+1

#Sentencia que permite saber si el numero de contornos es igual a 10 (numero total de pastillas)
if(len(cnts) >= 10):
	print("Pastillas completas")

#Sentencia que permite saber si el numero de contornos es diferente a 10 (numero total de pastillas)
elif (cnts == 10):
	print("Error pastillas incompletas")
cv2.destroyAllWindows()