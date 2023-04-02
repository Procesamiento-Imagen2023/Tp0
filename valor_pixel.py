import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('imagen.jpg')

# Función para mostrar el valor del pixel en una ventana
def mostrar_valor_pixel(event, x, y, flags, parametros):
    if event == cv2.EVENT_MOUSEMOVE:
        valor_pixel = imagen[y, x]
        ventana_texto = np.zeros((50, 200, 3), dtype=np.uint8)
        ventana_texto[:] = (255, 255, 255)
        fuente = cv2.FONT_HERSHEY_SIMPLEX
        escala_fuente = 0.5
        grosor_fuente = 1
        color_fuente = (0, 0, 0)
        texto_r = f"R: {valor_pixel[0]}"
        texto_g = f"G: {valor_pixel[1]}"
        texto_b = f"B: {valor_pixel[2]}"
        cv2.putText(ventana_texto, texto_r, (10, 20), fuente, escala_fuente, color_fuente, grosor_fuente, cv2.LINE_AA)
        cv2.putText(ventana_texto, texto_g, (10, 35), fuente, escala_fuente, color_fuente, grosor_fuente, cv2.LINE_AA)
        cv2.putText(ventana_texto, texto_b, (10, 50), fuente, escala_fuente, color_fuente, grosor_fuente, cv2.LINE_AA)
        cv2.imshow('Valor del pixel', ventana_texto)

def editar_valor_pixel(event, x, y, flags, parametros):
    if event == cv2.EVENT_LBUTTONDOWN:
        imagen[y, x] = (0, 0, 0)
        cv2.imshow('Imagen', imagen)
    
# Crear la ventana para mostrar la imagen y la ventana para mostrar el valor del pixel
cv2.namedWindow('Imagen')
cv2.imshow('Imagen', imagen)
cv2.namedWindow('Valor del pixel')
#cv2.setMouseCallback('Imagen', mostrar_valor_pixel)
cv2.setMouseCallback('Imagen', editar_valor_pixel)

# Esperar a que se presione una tecla
cv2.waitKey(0)

# Cerrar las ventanas
cv2.destroyAllWindows()