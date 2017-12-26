# Deteccion de movimiento con camara estatica
import cv2
import numpy as np


cap = cv2.VideoCapture('IcabMovimientoEscenaEstatica.mp4')

bg = cv2.createBackgroundSubtractorMOG2(500,100,True)


while (1):
    ret, frame = cap.read()

    fore = bg.apply(frame)
    back = bg.getBackgroundImage()

    erode_result = cv2.erode(fore,(3,3))
    dilate_result = cv2.dilate(erode_result,(3,3))
    foreCVT = cv2.cvtColor(dilate_result,cv2.COLOR_GRAY2BGR)
    resultBitwise = cv2.bitwise_and(frame,foreCVT)

    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break

    cv2.imshow("Frame",frame)
    cv2.imshow("Background", back)
    cv2.imshow("Foreground",resultBitwise)


cap.release()
cv2.destroyAllWindows()




