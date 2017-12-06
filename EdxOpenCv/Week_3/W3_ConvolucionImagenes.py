import cv2
import numpy as np

# import matplotlib import pyplot as plt
# Info:  http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html

# Nombre de la imagen que se va a cargar
NombreImagen = 'IMG.jpg'

# Cargamos la imagen y se comprueba que esta ok
src = cv2.imread(NombreImagen)

if src is None:
    print("Error al cargar la imagen: %s" % NombreImagen)
else:
    kernel = np.ones((5, 5), np.float32) / 25
    print('Kernel:', kernel)

    dst = cv2.filter2D(src, -1, kernel)

    #cv2.filter2D(src, dst, -1, kernel, cv2.Point(-1, -1), 0, cv2.BORDER_DEFAULT); c++

    # Mostrar la imagen
    cv2.namedWindow("src", cv2.WINDOW_NORMAL)
    cv2.imshow("src", src)

    cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
    cv2.imshow("dst", dst)
    # Esperar a pulsar una tecla
    cv2.waitKey(0)
