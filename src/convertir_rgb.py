import cv2

# Carga la imagen en RGB
imagen_rgb = cv2.imread("imagen_rgb.jpg")

# Convierte la imagen a HSV
imagen_hsv = cv2.cvtColor(imagen_rgb, cv2.COLOR_BGR2HSV)

# Divide la imagen HSV en sus componentes de canal
h, s, v = cv2.split(imagen_hsv)

# Muestra cada componente en ambas representaciones
cv2.imshow("H en HSV", h)
cv2.imshow("S en HSV", s)
cv2.imshow("V en HSV", v)

r, g, b = cv2.split(imagen_rgb)
cv2.imshow("R en RGB", r)
cv2.imshow("G en RGB", g)
cv2.imshow("B en RGB", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
