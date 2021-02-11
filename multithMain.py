import cv2
from mltith import *
import time
from PiCANRec import *



time.sleep(180)
#For deployment purposes uncoment the following try-exception 
#try:
#    dateTime()
#except Exception as e:
#    print('CAN BUS not working:{}'.format(str(e)))
cam1 = camera(0, True)
cam2 = camera(1, True)
cam3 = camera(3, True)
cam4 = camera(5, True)


start = time.time()
try:
    cam1.start()
    cam2.start()
    cam3.start()
    cam4.start()

except KeyboardInterrupt:

    cam1.workFinished()
    cam2.workFinished()
    cam3.workFinished()
    cam4.workFinished()

