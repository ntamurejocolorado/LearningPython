import cv2
import numpy as np
# Info: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html?highlight=matchtemplate
# Nombre de la imagen que se va a cargar
NombreImagen = 'corr_norm.tif'
NombreModelo = 'modelo.tif'

# Cargamos la imagen y comprobamos que ok
src = cv2.imread(NombreImagen)
templ = cv2.imread(NombreModelo)

if src is None:
	print("Error al cargar la imagen: %s" %NombreImagen)
if templ is None:
	print("Error al cargar el modelo: %s" %NombreModelo)
	
# Reservamos memoria para los diversos metodos
rows_src,cols_src,ch_src = src.shape
rows_templ,cols_templ,ch_templ = templ.shape

iwidth = cols_src - cols_templ + 1
iheight = rows_src - rows_templ + 1

for i in range(0,6):
	res = cv2.matchTemplate(src,templ,)