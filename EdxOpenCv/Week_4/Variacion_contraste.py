import cv2
import numpy as np
from matplotlib import pyplot as plt


# Nombre de la imagen que se va a cargar
NombreImagen = "ivvi_low_contrast.jpg"

# Cargamos las imagenes
src = cv2.imread(NombreImagen)
src = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

if src is None:
    print("Error al cargar las imagenes %s and %s" %NombreImagen)
else:
    histSize = [256]
    # rango del nivel de gris 0-255
    rangeHist = [0,255]

    # imagen del histograma
    hist_w = 512
    hist_h = 400
    #bin_w = hist_w / histSize

    # Crear una imagen histImage(hist_h,hist_w, CV_8UC3,Scalar(0,0,0))
    #histImage = np.zeros([hist_h, hist_w, 1], dtype=np.uint8)
    #equalizedHistImage = np.zeros([hist_h,hist_w,1],dtype = np.uint8)

    # Calcular el histograma
    originalHist = cv2.calcHist(src,[0],None,histSize,rangeHist)
    #b_hist = cv2.calcHist(b, [0], None, [256], [0, 256])

    # TO-DO:!
    # Mostrar los valores del histograma de la imagen original
    #print("Original histogram")
    #for h in histSize:
    #    binVal = originalHist.itemset(h)

    # Normalizar el resultado a [0, histImage.rows]
    normalized_hist = cv2.normalize(src, 0, hist_w, cv2.NORM_MINMAX)

    # Equalize histogram from a grayscale image
    equaliz_img = cv2.equalizeHist(src)
    equalized_hist = cv2.calcHist(equaliz_img,[0],None,histSize,rangeHist)

    # Normalizar el histograma ecualizado
    equalized_normalized_hist = cv2.normalize(equalized_hist,0,hist_w,cv2.NORM_MINMAX)

    # Dibujar los histogramas
    #for i in normalized_hist:
        #histr = cv2.calcHist([normalized_hist], [i], None, [256], [0, 256])
     #   plt.plot(normalized_hist, color=(255,0,0))
      #  plt.xlim([0, 256])

    # Dibujar para cada canal
    plt.plot(originalHist, color='b')
    plt.plot(equalized_hist, color='r')
    plt.xlim([0, 256])
    plt.show()

    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.imshow("Original", src)
    cv2.namedWindow("Equalized picture", cv2.WINDOW_NORMAL)
    cv2.imshow("Equalized picture", equaliz_img)

    cv2.waitKey(0)






