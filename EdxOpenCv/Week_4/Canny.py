# Canny:
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
    ImageCanny = cv2.Canny(src,100,150,3)

    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.imshow("Original", src)

    cv2.namedWindow("Canny", cv2.WINDOW_NORMAL)
    cv2.imshow("Canny", ImageCanny)

    # Esperar a pulsar una tecla
    cv2.waitKey(0)

