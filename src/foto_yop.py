import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Funcion para cargar la imagen
def cargar_imagen_raw():
    file_path = filedialog.askopenfilename(filetypes=[("RAW files", "*.raw")])
    if not file_path:
        return

    # Ventana de ancho y alto de la imagen
    input_window = tk.Toplevel(principal)
    input_window.title("Ingrese el tamaño de la imagen")
    input_window.geometry("300x150")
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
        img = np.fromfile(file_path, dtype=np.uint8, count=ancho*alto)
        img = np.reshape(img, (alto, ancho))
        cv2.imshow("Imagen", img)

    boton_aceptar = tk.Button(input_window, text="Aceptar", command=tamanio_imagen)
    boton_aceptar.grid(row=2, column=1)

# Funcion para guardar la imagen
def guardar_imagen():
    global img
    # Ruta de destino de la imagen
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("Imagen JPEG", "*.jpg"), ("Imagen PNG", "*.png")])
    # Guardar la imagen
    cv2.imwrite(file_path, img)

# Función para recortar una parte de la imagen
def crop_image(event, x, y, flags, param):
    global cropping, x_start, y_start, x_end, y_end
    # Si se presionó el botón izquierdo del mouse, comenzar a recortar
    if event == cv2.EVENT_LBUTTONDOWN:
        cropping = True
        x_start, y_start = x, y
    # Si se soltó el botón izquierdo del mouse, terminar el recorte
    elif event == cv2.EVENT_LBUTTONUP:
        cropping = False
        x_end, y_end = x, y
        # Iniciar el recorte
        start_cropping()

# Función para realizar el recorte
def start_cropping():
    global cropping, x_start, y_start, x_end, y_end, img_color
    # Definir el área de recorte
    x = min(x_start, x_end)
    y = min(y_start, y_end)
    w = abs(x_end - x_start)
    h = abs(y_end - y_start)
    # Recortar la imagen
    img_cropped = img_color[y:y+h, x:x+w]
    # Mostrar la imagen recortada en una ventana
    cv2.imshow("Imagen recortada", img_cropped)
    # Guardar la imagen recortada
    file_path = filedialog.asksaveasfilename(defaultextension=".raw")
    if file_path:
        with open(file_path, "wb") as f:
            f.write(img_cropped)
    # Cerrar la ventana de recorte
    cv2.destroyWindow("Recorte")

# Asociar la función de recorte a la ventana de imagen
cv2.namedWindow("Imagen")
cv2.setMouseCallback("Imagen", crop_image)

# Ventana principal
principal = tk.Tk()
principal.title("FotoYop")
principal.geometry("300x300")

# Menu
menu_bar = tk.Menu(principal)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir...", command=cargar_imagen_raw)
file_menu.add_command(label="Guardar...", command=guardar_imagen)
file_menu.add_command(label="Recortar...", command=start_cropping)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=principal.quit)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
principal.config(menu=menu_bar)

# Loop
principal.mainloop()