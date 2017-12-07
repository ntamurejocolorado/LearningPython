import cv2
import numpy as np
from matplotlib import pyplot as plt

# Info: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html?highlight=matchtemplate
# Nombre de la imagen que se va a cargar
NombreImagen = "IMG.jpg"
NombreModelo = "MM.jpg"

# Cargamos las imagenes
src = cv2.imread(NombreImagen)
templ = cv2.imread(NombreModelo)
w, h, c = templ.shape

if src is None or templ is None:
    print("Error al cargar las imagenes %s and %s" %(NombreImagen, NombreModelo))
else:
    iwidth = src.shape[1] - templ.shape[1] + 1
    iheight = src.shape[0] - templ.shape[0] + 1

    match_method = cv2.TM_SQDIFF_NORMED

    #Correlacion
    dst = cv2.matchTemplate(src,templ,match_method)
    dst = cv2.normalize(dst,dst,0,1,cv2.NORM_MINMAX,-1)

    min_Val,max_Val, min_Loc, max_Loc = cv2.minMaxLoc(dst)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if match_method is cv2.TM_SQDIFF or match_method is cv2.TM_SQDIFF_NORMED:
        top_left = min_Loc
    else:
        top_left = max_Loc

    bottom_right = (top_left[0] + w, top_left[1] + h )

    cv2.rectangle(src, top_left, bottom_right, 255, 2)

    cv2.imshow("src", src)
    cv2.imshow("Result", dst)
    cv2.imshow("templ", templ)


    cv2.waitKey(0)

