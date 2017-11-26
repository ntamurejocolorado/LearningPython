import cv2
import numpy as np

# Nombre de la imagen que se va a cargar

NombreImagen = 'ivvi_684x684_gray.jpg'

# Cargamos la imageny se comprueba quelo ha hecho correctamente

imagen = cv2.imread(NombreImagen)
if imagen is None:
    print("Error al cargar la imagen %s" %NombreImagen)
else:
    rows,columns,channels = imagen.shape
    # Las siguientes operaciones crea float en python
    # para poder acceder a los pixeles sera necesario que sean
    # de tipo int por tanto hacemos un casting a int
    # int(cuartoRows)
    cuartoRows = rows/4
    cuartoCols = columns/4
    maxRows = 3 * cuartoRows
    maxCols = 3 * cuartoCols

    # Opcion 1: elegimos el rango de la imagen y lo ponemos a cero.
    square = imagen[int(cuartoRows):int(maxRows),int(cuartoCols):int(maxCols)]
    imagen[int(cuartoRows):int(maxRows), int(cuartoCols):int(maxCols)] = 0

    # Opcion 2
    # Recorrer la imagen por filas y columnas y colocar los 3 canales a cero para que sea negro
    # for x in range(int(cuartoRows),int(maxRows)):
    #     for y in range(int(cuartoCols),int(maxCols)):
    #         imagen.itemset((x,y,0),0)
    #         imagen.itemset((x, y, 1), 0)
    #         imagen.itemset((x, y, 2), 0)

    # Mostrar la imagen
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.imshow("Original", imagen)

    # Guardar resultado
    cv2.imwrite("Resultado.jpg", imagen)

    cv2.waitKey(0)
