import cv2
import numpy as np

xI, yI, xF, yF = 0, 0, 0, 0
interuptor = False

def dibujar(event, x, y, flags, param):
    global xI, xF, yI, yF, interuptor, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        xI, yI = x, y
        interuptor = False

    if event == cv2.EVENT_LBUTTONUP:
        xF, yF = x, y
        interuptor = True
        
        recorte = img[yI:yF, xI:xF, :]
        print(recorte.shape)
        if recorte.shape[0] > 0 and recorte.shape[1] > 0:
            cv2.imwrite('recorte.jpg', img[yI:yF, xI:xF, :])

img=cv2.imread('imagen.jpg')
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen', dibujar)

while True:
    img = cv2.imread('imagen.jpg')
    if interuptor:
        cv2.rectangle(img, (xI, yI), (xF, yF), (0, 255, 0), 2)
    
    cv2.imshow('imagen', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
    