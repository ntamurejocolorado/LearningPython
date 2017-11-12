print("Drawing Functions in OpenCV")

# Learn to draw different geometric shapes with OpenCV
# We will learn these function: cv2.line(), cv2.circle(), cv2.rectangle(), cv2.ellipse(), cv2.putText()...

print("Drawing Line")

import  numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a circle
img = cv2.circle(img,(447,63),63,(0,0,255),-1)

# Draw a ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Draw a polygon
# To draw a polygon, first you need coordinates of vertices. Make those points into an array
# of shape ROWSx1x2 where ROWS are number of vertices and it should be of typ int32.
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))

img = cv2.polylines(img,[pts],True,(0,255,255))

# Aadding Text to Images

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)


cv2.namedWindow('Drawing',cv2.WINDOW_NORMAL)
cv2.imshow('Drawing',img)


# Write an image if you press 's' and exit without saving if you press Esc
k = cv2.waitKey(0) # esperamos hasta que se pulse una tecla
cv2.destroyAllWindows()


