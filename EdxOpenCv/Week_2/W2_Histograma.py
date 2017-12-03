import cv2
import numpy as np
from matplotlib import pyplot as plt

NombreImagen = 'ivvi_684x684.jpg'

# Cargamos la imagen y se comprueba que lo ha hecho correctamente
src = cv2.imread(NombreImagen)

if src is None:
    print("Error al cargar la imagen %s" % NombreImagen)

# Separar la imagen a 3 subimagenes (A,V y R)
b,g,r = cv2.split(src)


# Variables para el histograma
histSize = [256]

# Los rangos (A,V,R)
histRange = range(0, 256)

# Calcular el histograma
b_hist = cv2.calcHist(b, [0], None, [256], [0,256])
g_hist = cv2.calcHist(g, [1], None, [256], [0,256])
r_hist = cv2.calcHist(r, [2], None, [256], [0,256])

plt.hist(src.ravel(),256,[0,256])
plt.show()


#print("hist: ", b_hist)

# Dibujar el histograma para A, V y R
hist_w = 512
hist_h = 400
bin_w = 2

# Crear una imagen histImage(hist_h,hist_w, CV_8UC3,Scalar(0,0,0))
histImage = np.zeros([hist_h, hist_w, 3], dtype=np.uint8)

# Normalizar el resultado a [0, histImage.rows]
b_hist = cv2.normalize(b_hist, 0, 1, cv2.NORM_MINMAX)
g_hist = cv2.normalize(g_hist, 0, 1, cv2.NORM_MINMAX)
r_hist = cv2.normalize(r_hist, 0, 1, cv2.NORM_MINMAX)

#print("hist: ", b_hist)

# Dibujar para cada canal
plt.plot(b_hist,color = 'b')
plt.plot(g_hist,color = 'g')
plt.plot(r_hist,color = 'r')
plt.xlim([0,256])
plt.show()

# Mostrar la imagen
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", src)
    # cv2.namedWindow("Histograma", cv2.CV_WINDOW_AUTOSIZE)
    # cv2.imshow("Histograma", histImage)
    # Esperar a pulsar una tecla
cv2.waitKey(0)


