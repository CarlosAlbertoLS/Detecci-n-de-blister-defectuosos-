import cv2

img = cv2.imread('p13.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(imgray,25)
blur = cv2.GaussianBlur(median,(11,11),290)
_,th = cv2.threshold(blur, 82, 255, cv2.THRESH_BINARY)

cnts,_ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_HERSHEY_SIMPLEX
i=0
cv2.imshow("Contornos",th)

print('Contornos: ', len(cnts))
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
if(len(cnts) >= 10):
	print("Pastillas completas")
elif (cnts == 10):
	print("Error pastillas incompletas")
cv2.destroyAllWindows()