import cv2
import numpy as np

file_imagen = "../img"
file_path = f"{file_imagen}/cuadrado_blanco.png"


def create_image():
    # Crea la imagen en blanco
    img = np.zeros((200, 200), np.uint8)

    # Dibuja un cuadrado blanco
    x = y = 50
    w = h = 100
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)

    # Save the image to a file
    cv2.imwrite(file_path, img)

    return img
