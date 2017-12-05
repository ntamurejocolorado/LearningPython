import cv2
import numpy as np

NombreImagen = 'ivvi_684x684_gray.jpg'

# Cargamos la imagen y se comprueba que lo ha hecho correctamente
imagen = cv2.imread(NombreImagen)

if imagen is None:
    print("Error al cargar la imagen %s" % NombreImagen)
else:
    lut = np.zeros([1, 256,3], dtype=np.uint8)

    # Funcion inversa
    # for (int i = 0; i < 256; i++){
    #	lut.at<uchar>(i) = 255 - i; //Función Inversa
    # }
    #for i in range(0,256):
     #   lut.itemset(i, 255 - i)

    ImagenResultadoLUT = cv2.LUT(imagen, lut)

    # Mostrar la imagen
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.imshow("Original", imagen)
    cv2.namedWindow("ImagenResultadoLUT", cv2.WINDOW_NORMAL)
    cv2.imshow("ImagenResultadoLUT", ImagenResultadoLUT)
    # Esperar a pulsar una tecla
    cv2.waitKey(0)
