import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

from crear_imagen import create_image
from restar_images import restar_imagenes


# Funcion para cargar la imagen
def cargar_imagen_raw():
    file_path = filedialog.askopenfilename(
        filetypes=[("RAW files", "*.raw"), ("PGM files", "*.pgm"), ("PPM files", "*.ppm")])
    if not file_path:
        return

    # Ventana de ancho y alto de la imagen
    input_window = tk.Toplevel(principal)
    input_window.title("Ingrese el tamaño de la imagen")
    input_window.geometry("300x300")
    input_window.resizable(False, False)

    tk.Label(input_window, text="Ancho:").grid(row=0)
    tk.Label(input_window, text="Alto:").grid(row=1)

    valor_ancho = tk.Entry(input_window)
    valor_ancho.grid(row=0, column=1)

    valor_alto = tk.Entry(input_window)
    valor_alto.grid(row=1, column=1)

    def tamanio_imagen():
        global img
        ancho = int(valor_ancho.get())
        alto = int(valor_alto.get())
        input_window.destroy()

        # Leer imagen RAW y mostrarla
        img = np.fromfile(file_path, dtype=np.uint8, count=ancho * alto)
        img = np.reshape(img, (alto, ancho))
        # cv2.imshow(str(file_path), img)
        cv2.namedWindow('Imagen')
        cv2.imshow('Imagen', img)
        file_menu.entryconfig("Guardar", state="normal")
        file_menu.entryconfig("Recortar", state="normal")
        file_menu.entryconfig("Ver pixel", state="normal")

    boton_aceptar = tk.Button(input_window, text="Aceptar", command=tamanio_imagen)
    boton_aceptar.grid(row=2, column=1)


# Funcion para guardar la imagen
def guardar_imagen(imagen=None):
    # Ruta de destino de la imagen
    if imagen is None:
        imagen = img

    file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("Imagen JPEG", "*.jpg"), ("Imagen PNG", "*.png")])
    # Guardar la imagen
    cv2.imwrite(file_path, imagen)


def capturar_recorte():
    xI, yI, xF, yF = 0, 0, 0, 0
    interuptor = False

    def dibujar(event, x, y, flags, param):
        nonlocal xI, xF, yI, yF, interuptor

        if event == cv2.EVENT_LBUTTONDOWN:
            xI, yI = x, y
            interuptor = False

        if event == cv2.EVENT_LBUTTONUP:
            xF, yF = x, y
            interuptor = True

    cv2.setMouseCallback('Imagen', dibujar)

    while True:
        if interuptor:
            cv2.rectangle(img, (xI, yI), (xF, yF), (0, 255, 0), 2)
            recorte = img[yI:yF, xI:xF]
            print(recorte)
            cv2.imshow('Imagen', img)
            if recorte.shape[0] > 0 and recorte.shape[1] > 0:
                interuptor = False
                cv2.rectangle(img, (xI, yI), (xF, yF), (0, 0, 0), 0)
                cv2.imshow('Imagen nueva', recorte)
                guardar_imagen(recorte)

        cv2.imshow('Imagen', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()


def valor_pixel():
    def mostrar_valor_pixel(event, x, y, flags, parametros):
        if event == cv2.EVENT_MOUSEMOVE:
            valor_pixel = img[y, x]
            ventana_texto = np.zeros((50, 200), dtype=np.uint8)
            ventana_texto[:] = 255
            fuente = cv2.FONT_HERSHEY_SIMPLEX
            escala_fuente = 0.5
            grosor_fuente = 1
            color_fuente = 0
            texto = f"Valor de gris: {valor_pixel}"
            cv2.putText(ventana_texto, texto, (10, 25), fuente, escala_fuente, color_fuente, grosor_fuente, cv2.LINE_AA)
            cv2.imshow('Valor del pixel', ventana_texto)
        elif event == cv2.EVENT_RBUTTONDOWN:
            print("esta es la imagen", img[y, x])
            img[y, x] = (0)
            cv2.imshow('Imagen', img)

    cv2.setMouseCallback('Imagen', mostrar_valor_pixel)


# Ventana principal
principal = tk.Tk()
principal.title("FotoYop")
principal.geometry("300x300")

# Menu
menu_bar = tk.Menu(principal)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", command=cargar_imagen_raw)
file_menu.add_command(label="Guardar", command=guardar_imagen, state="disabled")
file_menu.add_command(label="Recortar", command=capturar_recorte, state="disabled")
file_menu.add_command(label="Ver pixel", command=valor_pixel, state="disabled")
file_menu.add_command(label="Crear imagen en blanco", command=create_image)
file_menu.add_command(label="Restar 2 imagenes", command=restar_imagenes)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=principal.quit)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
principal.config(menu=menu_bar)

# Loop
principal.mainloop()
