import cv2
from camera import *
import time



cam1 = camera(200)
#cam2 = camera(1)
#picam = piCamera()

time.sleep(2)
start = time.time()
try:
    while(True):
        
            
        frame1, _ = cam1.PicTime(True)
        #frame2, _ = cam2.PicTime(False)
        #frame3, _ = picam.PicTime(True)

        #cv2.imshow('frame1',frame1)
        #cv2.imshow('frame2',frame2)
        #cv2.imshow('frame2',frame3)

except KeyboardInterrupt:

    finish = time.time()
    print('\nWebcam%i Captured %d frames at %.2ffps' % (
    cam1.camera_id,
    cam1.i,
    cam1.i / (finish - start)))
    print('Time:{}'.format(finish - start))
    
    #print('\nPiCam Captured %d frames at %.2ffps' % (
    #picam.i,
    #picam.i / (finish - start)))
    #print('Time:{}'.format(finish - start))

    cam1.workFinished()
    #cam2.workFinished()
    #picam.workFinished()
