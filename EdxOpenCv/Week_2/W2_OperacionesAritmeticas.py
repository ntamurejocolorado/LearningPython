import cv2
import numpy as np

# Nombre de la imagen que se va a cargar
NombreImagen1 = 'LSI.jpg'
NombreImagen2 = 'UC3M.jpg'

# Cargamos la imagen y se comprueba que lo ha hecho ok
img1 = cv2.imread(NombreImagen1)
img2 = cv2.imread(NombreImagen2)

if img1 is None or img2 is None:
    print("Error al cargar las imagenes %s and %s" % (NombreImagen1, NombreImagen2))
else:
    cv2.imshow("Image1", img1)
    cv2.imshow("Image2", img2)

    # dst = cv2.addWeighted(img1,1,img2,1,0)
    dst = cv2.add(img1, img2)
    cv2.imshow("ADD", dst)

    dst = cv2.subtract(img1,img2)
    cv2.imshow("SUBSTRACT",dst)

    dst = cv2.multiply(img1,img2,dst,1)
    cv2.imshow("MULTIPLY",dst)

    dst = cv2.divide(img1,img2)
    cv2.imshow("DIVIDE",dst)
    cv2.waitKey(0)





