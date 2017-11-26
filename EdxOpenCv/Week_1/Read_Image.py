import cv2

# Nombre de la imagen que se va a cargar
NombreImage = 'ivvi2.jpg'

# Cargamos la imagen y se comprueba que lo ha hecho correctamente
imagen = cv2.imread(NombreImage) # 0 grayscale, 1 in color
print (imagen)

if imagen is None:
    print("Error al cargar la imagen %s" %NombreImage)
else:
    # Mostrar imagen
    cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
    cv2.imshow("Original",imagen)


    # Write an image if you press 's' and exit without saving if you press Esc
    k = cv2.waitKey(0) # esperamos hasta que se pulse una tecla
    if k == 27:
        cv2.destroyAllWindows()
