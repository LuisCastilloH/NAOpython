# Credits to different examples found online

import cv2,time,argparse,glob
import numpy as np

def onTrackbarActivity(x):
    pass

if __name__ == '__main__' :
    cap = cv2.VideoCapture(0)

    #creating windows to display images
    cv2.namedWindow('SelectHSV',cv2.WINDOW_AUTOSIZE)

    #creating trackbars to get values for HSV
    cv2.createTrackbar('HMin','SelectHSV',0,180,onTrackbarActivity)
    cv2.createTrackbar('HMax','SelectHSV',0,180,onTrackbarActivity)
    cv2.createTrackbar('SMin','SelectHSV',0,255,onTrackbarActivity)
    cv2.createTrackbar('SMax','SelectHSV',0,255,onTrackbarActivity)
    cv2.createTrackbar('VMin','SelectHSV',0,255,onTrackbarActivity)
    cv2.createTrackbar('VMax','SelectHSV',0,255,onTrackbarActivity)

    while(1):
        _, frame = cap.read()
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
        HMin = cv2.getTrackbarPos('HMin','SelectHSV')
        SMin = cv2.getTrackbarPos('SMin','SelectHSV')
        VMin = cv2.getTrackbarPos('VMin','SelectHSV')
        HMax = cv2.getTrackbarPos('HMax','SelectHSV')
        SMax = cv2.getTrackbarPos('SMax','SelectHSV')
        VMax = cv2.getTrackbarPos('VMax','SelectHSV')
        minHSV = np.array([HMin, SMin, VMin])
        maxHSV = np.array([HMax, SMax, VMax])

        # Convert the BGR image to other color spaces
        imageHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # Create the mask using the min and max values obtained from 
        # trackbar and apply bitwise and operation to get the results                     
        maskHSV = cv2.inRange(imageHSV,minHSV,maxHSV)
        resultHSV = cv2.bitwise_and(frame, frame, mask = maskHSV)
        
        cv2.imshow('SelectHSV',resultHSV)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()



