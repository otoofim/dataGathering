import numpy as np
import cv2
from datetime import datetime
import picamera
import picamera.array
import os



class camera:

    def __init__(self, cam_num):
        
        self.camera_id = cam_num
        self.cap = cv2.VideoCapture(cam_num)
        self.i = 0
        date = datetime.now()
        #self.cap.set(cv2.CAP_PROP_FPS, int(60))
        
        base_add = '/home/pi/Desktop/test/'
        if not os.path.exists(base_add + "cam{}".format(self.camera_id)):
            os.mkdir(base_add + '/cam{}'.format(self.camera_id))
        if not os.path.exists(base_add + 'cam{}/{}'.format(self.camera_id, date.strftime('%y.%m.%d'))):
            os.mkdir(base_add + 'cam{}/{}'.format(self.camera_id, date.strftime('%y.%m.%d')))

        self.save_add = base_add + 'cam{}/{}/'.format(self.camera_id, date.strftime('%y.%m.%d'))

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

    def PicTime(self, save = True):
        frame, now = self.getFrame()
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(frame, str(now),(frame.shape[1] - 200, frame.shape[0] - 10), font, 0.7,(255,255,255),2,cv2.LINE_AA)
        if save:
            cv2.imwrite(self.save_add + '{}.png'.format(datetime.now().strftime('%H.%M.%S.%f')), frame)
        self.i += 1
        return frame, now

    def workFinished(self):
        self.cap.release()
        cv2.destroyAllWindows()
        
        
        
# class piCamera:
# 
#     def __init__(self):
#         try:
#             self.i = 0
#             self.camera_id = 'PiCam'
#             self.cap = picamera.PiCamera()
#             self.cap.resolution = (1024, 768)
#             self.cap.framerate = 60
#             #self.cap.exposure_mode = 11
#             self.stream = picamera.array.PiRGBArray(self.cap)
#                         
#         except:
#             print('PiCam is not detected!')
#             exit()
#         date = datetime.now()
#         if not os.path.exists("/home/pi/ssd/winter2021/{}".format(self.camera_id)):
#             os.mkdir('/home/pi/ssd/winter2021/{}'.format(self.camera_id))
#         if not os.path.exists('/home/pi/ssd/winter2021/{}/{}'.format(self.camera_id, date.strftime('%y.%m.%d'))):
#             os.mkdir('/home/pi/ssd/winter2021/{}/{}'.format(self.camera_id, date.strftime('%y.%m.%d')))
# 
#         self.save_add = '/home/pi/ssd/winter2021/{}/{}/'.format(self.camera_id, date.strftime('%y.%m.%d'))
#         
# 
#     def IsCamAva(self):
#         if self.cap:
#             return True
#         else:
#             return False
# 
# 
#     def getFrame(self):
#         if self.IsCamAva():
#             now = datetime.now().time()
#             self.cap.capture(self.stream, format='bgr',use_video_port=True)
#             frame = self.stream.array
#             self.stream.truncate()
#             self.stream.seek(0)
#             if frame is not None:
#                 return frame, now
#             else:
#                 print("Frame can not be retrieved.")
#         else:
#             print("The camera is not available.")
# 
#     def PicTime(self, save = True):
#         frame, now = self.getFrame()
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(frame, str(now),(frame.shape[1] - 200, frame.shape[0] - 10), font, 0.7,(255,255,255),2,cv2.LINE_AA)
#         if save:
#             cv2.imwrite(self.save_add + '{}.png'.format(datetime.now().strftime('%H.%m.%S.%f')), frame)
#             #cv2.imwrite(self.save_add + '{}.png'.format('tt'), frame)
#         self.i += 1
#         return frame, now
# 
#     def workFinished(self):
#         cv2.destroyAllWindows()

              
        
        
        
        

