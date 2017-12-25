# Sobel:
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Nombre de la imagen que se va a cargar
NombreImagen = "ivvi_684x684_gray.jpg"

# Cargamos las imagenes
src = cv2.imread(NombreImagen)

if src is None:
    print("Error al cargar la imagen %s and %s" %NombreImagen)
else:
    w, h, c = src.shape
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S

    # Gaussian blur
    src = cv2.blur(src, (3, 3), 0)

    # Gradiente X
    grad_x = cv2.Sobel(src,ddepth,1,0,None,3,scale,delta,cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)

    # Gradiente Y
    grad_y = cv2.Sobel(src, ddepth, 0, 1, None, 3, scale, delta, cv2.BORDER_DEFAULT)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    # Total Gradiente (aproximado)
    grad = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)
    _,grad = cv2.threshold(grad,80,255,cv2.THRESH_BINARY)

    # Nota: en el threshold ponemos como salida _,grad porque el threshold devuelve
    # dos valores y añade una variable extra.Por tanto, debe ser la salida así porque
    # la imagen sobre la que se aplica es el segundo valor que devuelve.

    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.imshow("Original", src)

    cv2.namedWindow("Sobel", cv2.WINDOW_NORMAL)
    cv2.imshow("Sobel", grad)

    # Esperar a pulsar una tecla
    cv2.waitKey(0)
