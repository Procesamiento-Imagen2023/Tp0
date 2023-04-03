import cv2
import numpy as np
from tkinter import filedialog
from tkinter import *
import os


def abrir_imagen():
    file_path = filedialog.askopenfilename()
    return file_path


root = Tk()
root.filename1 = abrir_imagen()
root.filename2 = abrir_imagen()
root.withdraw()

img1_size = os.path.getsize(root.filename1)
img2_size = os.path.getsize(root.filename2)

if img1_size != img2_size:
    print("Las imagenes no tienen el mismo tamaño")
else:
    img1 = np.fromfile(root.filename1, dtype=np.uint8)
    img2 = np.fromfile(root.filename2, dtype=np.uint8)

    img1 = np.reshape(img1, (200, 200))  # cambiar las dimensiones según la imagen
    img2 = np.reshape(img2, (200, 200))

    # resta de imágenes
    img3 = cv2.absdiff(img1, img2)

    cv2.imshow("Resultado de la resta", img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
