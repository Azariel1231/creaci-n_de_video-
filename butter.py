import cv2

#importar imagen
image = cv2.imread("butterfly.jpg")

#mostar imagen a color
cv2.imshow("mostrar imagen", image)

print(image)

cv2.waitKey(0)