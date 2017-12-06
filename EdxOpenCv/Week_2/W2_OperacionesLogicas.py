import cv2
import numpy as np

# Crear las imagenes
img1 = np.zeros([200,400],dtype=np.uint8)
img2 = np.zeros([200,400],dtype=np.uint8)

# Creamos las máscaras con partes blancas en las imagenes anteriores
#rows = [0:400] #range(0,399) #img1.shape[0])
#cols = [0:100] #range(0,100) #int(img1.shape[1]/2))

img1[0:img1.shape[0],0:int(img1.shape[1]/2)] = 255
cv2.imshow('img1',img1)

img2[100:150,150:350] = 255
cv2.imshow('img2',img2)

res = cv2.bitwise_and(img1,img2)
cv2.imshow("AND",res)

res = cv2.bitwise_or(img1,img2)
cv2.imshow("OR",res)

res = cv2.bitwise_xor(img1,img2)
cv2.imshow("XOR",res)

res = cv2.bitwise_not(img1)
cv2.imshow("NOT",res)


cv2.waitKey(0)
