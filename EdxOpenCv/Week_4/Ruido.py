import cv2
import numpy as np


# Nombre de la imagen que se va a cargar
NombreImagen = "ivvi_512x512_gray_rg.jpg"
NombreImagenIvvi = "ivvi_512x512_gray.jpg"

# Cargamos las imagenes
src = cv2.imread(NombreImagen)
ivvi = cv2.imread(NombreImagenIvvi)

if src is None or ivvi is None:
    print("Error al cargar las imagenes %s and %s" %(NombreImagen, ivvi))
else:
    # Homogeneous blur
    imgBlr = cv2.blur(src,(5,5),4)

    # Gaussian blur
    imgGus = cv2.GaussianBlur(src,(5,5),0,0,4)

    # Median blur
    imgMed = cv2.medianBlur(src,5)

    # Bilateral filter
    imgBil = cv2.bilateralFilter(src,15,80,80)

    # Mostrar la imagenes
    cv2.namedWindow("Vehiculo IVVI", cv2.WINDOW_NORMAL)
    cv2.imshow("Vehiculo IVVI", ivvi)

    cv2.namedWindow("Original con ruido", cv2.WINDOW_NORMAL)
    cv2.imshow("Original con ruido", src)

    cv2.namedWindow("blur", cv2.WINDOW_NORMAL)
    cv2.imshow("blur", imgBlr)

    cv2.namedWindow("Gaussian", cv2.WINDOW_NORMAL)
    cv2.imshow("Gaussian", imgGus)

    cv2.namedWindow("Median", cv2.WINDOW_NORMAL)
    cv2.imshow("Median", imgMed)

    cv2.namedWindow("Bilateral", cv2.WINDOW_NORMAL)
    cv2.imshow("Bilateral", imgBil)

    cv2.waitKey(0)

