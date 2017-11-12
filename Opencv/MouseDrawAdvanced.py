# Mouse Advanced

# We draw either rectangles or circles (depending on the mode we select)
# by dragging the mouse like we do in Paint application.
# So our mouse callback function has two parts, one to draw rectangle and
# other to draw the circles.

import  cv2
import numpy as np


drawing = False # True if mouse is pressed
mode = True # If True, draw rectangle. Pres 'm' to toggle to curve
ix,iy = -1,-1

# Mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)



img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('Image')
cv2.setMouseCallback('Image',draw_circle)

while(1):
    cv2.imshow('Image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord ('m'): # Esto es si pulsamos la tecla "m" entonces cambia el modo
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()


















