import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Funcion para cargar la imagen
def cargar_imagen_raw():
    global file_path, img
    cv2.destroyAllWindows()
    file_path = filedialog.askopenfilename(filetypes=[("RAW files", "*.raw"),("PGM files", "*.pgm"),("PPM files", "*.ppm"), ("JPG files", "*.jpg")])
    es_raw()
    if not file_path:
        return

# Ventana de ancho y alto de la imagen
def ventana_tamanio():
    global input_window, valor_ancho, valor_alto
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
    
    boton_aceptar = tk.Button(input_window, text="Aceptar", command=imagen_raw)
    boton_aceptar.grid(row=2, column=1)

# Leer imagen RAW y mostrarla
def es_raw():
    global ancho, alto, flag
    flag = False
    img = cv2.imread(file_path)
    if(img is None):
        ventana_tamanio()
        flag = True
    else:
        imagen_rgb()
    file_menu.entryconfig("Promedio", state="normal")
    
# Formato de imagen RAW
def imagen_raw():
    global img, ancho, alto
    ancho = int(valor_ancho.get())
    alto = int(valor_alto.get())
    input_window.destroy()
    img = np.fromfile(file_path, dtype=np.uint8, count=ancho*alto)
    img = np.reshape(img, (alto, ancho))
    cv2.namedWindow('Imagen')
    cv2.imshow('Imagen', img)

# Formato de imagen RGB
def imagen_rgb():
    global img
    img = cv2.imread(file_path)
    cv2.namedWindow('Imagen')
    cv2.imshow('Imagen', img)

# Promedio de la imagen
def promedio():
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
            cv2.rectangle(img, (xI, yI), (xF, yF), (0, 255, 0), 1)
            recorte = img[yI:yF, xI:xF]
            print(recorte)
            cv2.imshow('Imagen', img)
            if recorte.shape[0] > 0 and recorte.shape[1] > 0:
                interuptor = False
                cv2.rectangle(img, (xI, yI), (xF, yF), (0, 0, 0), 0)
                if flag:
                    alto, ancho = recorte.shape[:2]
                    promedio = round(np.mean(recorte),2)
                    total_pixles = alto*ancho
                    print("Ancho: ", ancho)
                    print("Alto: ", alto)
                    print("Total de pixeles: ", total_pixles)
                    print("Promedio Grises: ", promedio)
                    ventana_promedio(ancho, alto, total_pixles, promedio)
                else:
                    alto, ancho = recorte.shape[:2]
                    total_pixles = alto*ancho
                    promedio = np.mean(recorte, axis=(0,1))
                    promR = round(promedio[0],2)
                    promG = round(promedio[1],2)
                    promB = round(promedio[2],2)
                    prom_total = round((promR + promG + promB)/3,2)
                    prom_individual = f"B: {promR}, G: {promG}, R: {promB}, Promedio total: {prom_total}"
                    print("Ancho: ", ancho)
                    print("Alto: ", alto)
                    print("Total de pixeles: ", prom_individual)
                    print("Promedio Color: ", total_pixles)
                    ventana_promedio(ancho, alto, total_pixles, prom_individual)
                    
        cv2.imshow('Imagen', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

def ventana_promedio(ancho, alto, total_pixles, promedio):
    ventana_texto = np.zeros((100, 600), dtype=np.uint8)
    ventana_texto[:] = 255
    fuente = cv2.FONT_HERSHEY_SIMPLEX
    escala_fuente = 0.5
    grosor_fuente = 1
    color_fuente = 0
    texto = f"Ancho: {ancho}"
    texto2 = f"Alto: {alto}"
    texto3 = f"Total de pixels: {total_pixles}"
    texto4 = f"Promedio : {promedio}"
    cv2.putText(ventana_texto, texto,  (10, 25), fuente, escala_fuente, color_fuente, grosor_fuente, cv2.LINE_AA)
    cv2.putText(ventana_texto, texto2, (10, 45), fuente, escala_fuente, color_fuente, grosor_fuente, cv2.LINE_AA)
    cv2.putText(ventana_texto, texto3, (10, 65), fuente, escala_fuente, color_fuente, grosor_fuente, cv2.LINE_AA)
    cv2.putText(ventana_texto, texto4, (10, 85), fuente, escala_fuente, color_fuente, grosor_fuente, cv2.LINE_AA)
    cv2.imshow('Promedio de pixels', ventana_texto)

# Ventana principal
principal = tk.Tk()
principal.title("Promedio")
principal.geometry("300x300")

# Menu
menu_bar = tk.Menu(principal)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", command=cargar_imagen_raw)
file_menu.add_command(label="Promedio", command=promedio, state="disabled")
file_menu.add_separator()
file_menu.add_command(label="Salir", command=principal.quit)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
principal.config(menu=menu_bar)

# Loop
principal.mainloop()
