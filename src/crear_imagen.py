import datetime

import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Directorio donde se guardara la imagen
file_imagen = "../img"

# Genera el nombre de la imagen usando la fecha y a hora actual
now = datetime.datetime.now()
file_name = f"cuadrado_blanco_{now.strftime('%Y%m%d_%H%M%S')}.png"
file_path = f"{file_imagen}/{file_name}"


# Funcion para crear la imagen en blanco con un cuadrado negro en el centro
def create_image():
    # Crea la imagen en blanco
    img = np.zeros((200, 200), np.uint8)

    # Dibuja un cuadrado blanco
    x = y = 50
    w = h = 100
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)

    # Guarda la imagen en un archivo
    cv2.imwrite(file_path, img)

    return img


# Interfaz para la creacion de la imagen

global img_tk


def show_imagen(img):
    global img_tk

    # Convierte la imagen de formato OpenCV a formato PIL
    img_pil = Image.fromarray(img)

    # Crea un objeto ImagenTk para mostrar la imagen en una ventana
    img_tk = ImageTk.PhotoImage(img_pil)

    # Crea la ventana
    window = tk.Tk()

    # Agrega un widget label para mostrar la imagen
    label = tk.Label(window, image=img_tk)
    label.pack()

    # Ejecuta el bucle principal de Tkinter
    window.mainloop()


# funcion que crea y muestra la imagen
def create_and_show_image():
    img = create_image()
    show_imagen(img)


# Crea una ventana con un boton que llama a la funcion de crear la imagen
window = tk.Tk()
button = tk.Button(window, text="Crear imagen", command=create_and_show_image)
button.pack()

# Ejecuta el bucle principal de Tkinter
window.mainloop()
