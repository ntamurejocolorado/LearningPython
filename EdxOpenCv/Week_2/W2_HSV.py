import cv2
import numpy as np

NombreImagen = 'ivvi_684x684.jpg'

# Cargamos la imagen y se comprueba que lo ha hecho correctamente
imRGB = cv2.imread(NombreImagen)

if imRGB is None:
    print("Error al cargar la imagen %s" % NombreImagen)
else:
    # Separar la imagen a 3 subimagenes
    b, g, r = cv2.split(imRGB)

    # Cambiamos el espacio de color
    imHSV = cv2.cvtColor(imRGB, cv2.COLOR_BGR2HSV)

    # Separamos los planos de hsv
    h, s, v = cv2.split(imHSV)

    # Mostrar la imagen
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.imshow("Original", imRGB)

    cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
    cv2.imshow("HSV", imHSV)
    cv2.waitKey(0)