# Realce de bordes
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
    # Crear una imagen
    ImagenFilt = np.zeros([h, w, c],dtype=np.uint8)
    ImagenFilt_1 = np.zeros([h, w, c], dtype=np.uint8)
    ImagenFilt_2 = np.zeros([h, w, c], dtype=np.uint8)

    # Crear kernel de unos
    kernel = np.array(([-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]),dtype=int)

    kernel_1 = np.array(([0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]), dtype=int)

    kernel_2 = np.array(([-1, -2, -1],
                       [-2, 13, -2],
                       [-1, -2, -1]), dtype=int)

    # Aplicamos el kernel sobre nuestra imagen con la funcion filter2D
    ImagenFilt = cv2.filter2D(src,-1,kernel)
    ImagenFilt_1 = cv2.filter2D(src, -1, kernel_1)
    ImagenFilt_2 = cv2.filter2D(src, -1, kernel_2)

    # Mostramos el resultado
    # Mostrar la imagen
    cv2.namedWindow("Imagen Original", cv2.WINDOW_NORMAL)
    cv2.imshow("Imagen Original", src)

    cv2.namedWindow("Imagen con realce de bordes", cv2.WINDOW_NORMAL)
    cv2.imshow("Imagen con realce de bordes", ImagenFilt)

    cv2.namedWindow("Imagen con realce de bordes kernel 1", cv2.WINDOW_NORMAL)
    cv2.imshow("Imagen con realce de bordes kernel 1", ImagenFilt_1)

    cv2.namedWindow("Imagen con realce de bordes kernel 2", cv2.WINDOW_NORMAL)
    cv2.imshow("Imagen con realce de bordes kernel 2", ImagenFilt_2)

    # Esperar a pulsar una tecla
    cv2.waitKey(0)




