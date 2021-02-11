import io
import itertools
import picamera
from datetime import datetime
import os

class piCamera:

    def __init__(self):
        try:
            self.i = 0
            self.camera_id = 'PiCam'
            self.cap = picamera.PiCamera()
            self.cap.resolution = (1024, 768)
            self.cap.framerate = 30
        except:
            print('PiCam is not detected!')
            exit()
        date = datetime.now()
        if not os.path.exists("/home/pi/ssd/winter2021/{}".format(self.camera_id)):
            os.mkdir('/home/pi/ssd/winter2021/{}'.format(self.camera_id))
        if not os.path.exists('/home/pi/ssd/winter2021/{}/{}'.format(self.camera_id, date.strftime('%y.%m.%d'))):
            os.mkdir('/home/pi/ssd/winter2021/{}/{}'.format(self.camera_id, date.strftime('%y.%m.%d')))

        self.save_add = '/home/pi/ssd/winter2021/{}/{}/'.format(self.camera_id, date.strftime('%y.%m.%d'))
        

    def outputs(self):
        yield io.open(self.save_add + datetime.now().strftime('%H.%m.%S.%f') + '.h264', 'wb')


    def getFrame(self):
        try:
            for output in self.cap.record_sequence(
                    self.outputs(), quality = 20, bitrate = 750000):
                while output.tell() < 20971520:
                    self.cap.wait_recording(0.1)
            
        except KeyboardInterrupt:
            exit()


if __name__ == '__main__':
    camera = piCamera()
    camera.getFrame()
