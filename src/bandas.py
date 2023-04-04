import cv2
import numpy as np

# Carga la imagen
img_rgb = cv2.imread('bandas.jpg', 1)

# Convierte de RGB a HSV
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

# Divide RGB en tres bandas (R, G, B)
r, g, b = cv2.split(img_rgb)

# Divide HSV en tres bandas (H, S, V)
h, s, v = cv2.split(img_hsv)

# Muestra cada banda en el sistema RGB
cv2.imshow('Rojo', r)
cv2.imshow('Verde', g)
cv2.imshow('Azul', b)

# Muestra cada banda en el sistema HSV
cv2.imshow('Matiz', h)
cv2.imshow('Saturacion', s)
cv2.imshow('Valor', v)

cv2.waitKey(0)
cv2.destroyAllWindows()