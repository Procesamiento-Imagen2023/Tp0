import cv2
import imagen as imagen

imagen = cv2.imread("imagen.jpg")
def mouse_callback(event, x, y, flags, param):
    global imagen_copia
    if event == cv2.EVENT_LBUTTONDOWN:
        # Obtiene la región seleccionada por el usuario
        region = imagen[y-10:y+10, x-10:x+10]
        cantidad_pixeles = region.shape[0] * region.shape[1]
        if len(region.shape) == 2:
            promedio_gris = int(region.mean())
            print(f"Cantidad de píxeles: {cantidad_pixeles}, Promedio de gris: {promedio_gris}")
        else:
            print("Error: la región seleccionada no es una imagen en escala de grises ni en color.")

# Crea una copia de la imagen para mostrar la selección del usuario
imagen_copia = imagen.copy()

# Muestra la imagen y espera a que el usuario seleccione una región
cv2.imshow("Imagen", imagen_copia)
cv2.setMouseCallback("Imagen", mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()