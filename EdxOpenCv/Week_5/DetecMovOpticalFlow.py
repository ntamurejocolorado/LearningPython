import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 500,
                       qualityLevel = 0.01,
                       minDistance = 10,
                       blockSize = 3 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (11,11),
                  maxLevel = 5,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
#color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
img_prev = old_frame;
#old_gray = cv2.cvtColor(img_prev, cv2.COLOR_BGR2GRAY)
#cornersA = cv2.goodFeaturesToTrack(img_prev, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(1):
    ret,frame = cap.read()
    #frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_next = frame;
    grayA = cv2.cvtColor(img_prev, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(img_next, cv2.COLOR_BGR2GRAY)

    cornersA = cv2.goodFeaturesToTrack(grayA, mask=None, **feature_params)

    # calculate optical flow
    cornersB, st, err = cv2.calcOpticalFlowPyrLK(grayA, grayB, cornersA, None, **lk_params)

    # Select good points
    good_new = cornersB[st==1]
    good_old = cornersA[st==1]

    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        #mask = cv2.line(mask, (a,b),(c,d), (255,0,0), 2)
        #frame = cv2.circle(frame,(a,b),5,(0,255,0),-1)
        img_prev = cv2.line(img_prev,(a,b),(c,d),(255,0,0),2)
    #img = cv2.add(frame,mask)

    #cv2.imshow('frame',img)
    cv2.imshow("Corners A", img_prev)
    cv2.imshow("Corners B", img_next)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points
    #old_gray = frame_gray.copy()
    img_prev = img_next;
    #cornersA = good_new.reshape(-1,1,2)

img_prev.release()
img_next.release()
grayB.release()
grayA.release()
cv2.destroyAllWindows()
cap.release()
