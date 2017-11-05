import numpy as np
import cv2

# Load and color image in grayscale

img = cv2.imread('image.jpg',0) # 0 grayscale, 1 in color

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)


# Write an image if you press 's' and exit without saving if you press Esc
k = cv2.waitKey(0) # esperamos hasta que se pulse una tecla
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("paris_guardada.png",img) # This will save the image in PNG format in the working directory
    cv2.destroyAllWindows()


