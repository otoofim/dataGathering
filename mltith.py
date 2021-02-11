import cv2
import threading
import numpy as np
from datetime import datetime
import picamera
import picamera.array
import os



class camera(threading.Thread):

    def __init__(self, cam_num, save = True):
        
        threading.Thread.__init__(self)
        self.camera_id = cam_num
        self.cap = cv2.VideoCapture(cam_num)
        self.i = 0
        self.save = save
        self.width = 480
        self.height = 640
        self.cap.set(3, self.height)
        self.cap.set(4, self.width)
        date = datetime.now()
        
        
        if not os.path.exists("/home/pi/ssd/winter2021/cam{}".format(self.camera_id)):
            os.mkdir('/home/pi/ssd/winter2021/cam{}'.format(self.camera_id))
        if not os.path.exists('/home/pi/ssd/winter2021/cam{}/{}'.format(self.camera_id, date.strftime('%y.%m.%d'))):
            os.mkdir('/home/pi/ssd/winter2021/cam{}/{}'.format(self.camera_id, date.strftime('%y.%m.%d')))

        self.save_add = '/home/pi/ssd/winter2021/cam{}/{}/'.format(self.camera_id, date.strftime('%y.%m.%d'))

    def IsCamAva(self):
        return self.cap.isOpened()


    def getFrame(self):
        if self.IsCamAva():
            now = datetime.now().time()
            ret, frame = self.cap.read()
            if ret:
                return frame, now
            else:
                print("Frame can not be retrieved.")
        else:
            print("The camera is not available.")

    def PicTime(self):
        try:
            frame, now = self.getFrame()
            frame = cv2.resize(frame, (self.height, self.width), interpolation = cv2.INTER_AREA)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, str(now),(frame.shape[1] - 200, frame.shape[0] - 10), font, 0.6,(255,255,255),2,cv2.LINE_AA)
            if self.save:
                cv2.imwrite(self.save_add + '{}.jpeg'.format(datetime.now().strftime('%H.%M.%S.%f')), frame)
            self.i += 1
            return frame, now
        except Exception as e:
            
            f = open("/home/pi/Desktop/logcam{}.txt".format(str(self.camera_id)), "a")
            f.write(str(e) + "\n")
            f.close()
            #print(e)

    def workFinished(self):
        self.cap.release()
        cv2.destroyAllWindows()
        
    def run(self):
        while True:
            cv2.waitKey(100)
            self.PicTime() 

