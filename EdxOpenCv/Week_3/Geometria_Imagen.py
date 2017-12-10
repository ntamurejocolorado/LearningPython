import cv2
import numpy as np

#Nombre de la imagen
NombreImagen = "IVVI.jpg"

#Carga imagen
src = cv2.imread(NombreImagen)
if src is None:
    print("Error en la imagen %s" %NombreImagen)
else:
    cv2.imshow("src",src)
    rows,cols,channel = src.shape

    #Scale
    dst = cv2.resize(src,None, fx =0.5,fy =0.5,interpolation = cv2.INTER_LINEAR)
    cv2.imshow("scale", dst)

    #Translation
    M = np.float32([[1,0,100],[0,1,50]]) #Matriz para hacer la traslación
    dst = cv2.warpAffine(src,M,(cols,rows))
    cv2.imshow("traslation",dst)

    # Rotate
    M = cv2.getRotationMatrix2D((cols/2,rows/2),60,1)
    dst = cv2.warpAffine(src,M,(cols,rows))
    cv2.imshow("Rotation",dst)
    # Reflection
    cv2.flip(src,1,dst)
    cv2.imshow("Reflection",dst)

    #Waiting...
    cv2.waitKey(0)