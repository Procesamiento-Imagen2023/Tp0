import cv2

# Imagenes a restar
img1 = cv2.imread('lena1.jpeg')
img2 = cv2.imread('lena2.jpeg')

# Resta de las imagenes
resta = cv2.subtract(img1, img2)

# Resultado
cv2.imshow('Imagen Restada', resta)
print(resta)
cv2.waitKey(0)
cv2.destroyAllWindows()