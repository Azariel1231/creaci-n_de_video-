import cv2

#importar imagen
img = cv2.imread("butterfly.jpg")

#mostar imagen a color
cv2.imshow("mostrar imagen", img)

#convertir imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#mostar imagen en escala de grises
cv2.imshow("escala de grises", gray)

print(gray)

cv2.waitKey(0)