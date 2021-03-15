import can
import subprocess
import datetime
from timeout import timeout

@timeout(60)
def dateTime():
    can_interface = 'can0'
    bus = can.interface.Bus(can_interface, bustype='socketcan')

    while True:
        print('Waiting for CAN BUS...')
        message = bus.recv()
        if int(message.arbitration_id) == 1536:
            time = list(message.data)
            year = time[0] + (time[1]*100)
            month = time[2]
            day = time[3]
            s = time[5] + (time[4]*0.01)
            minute = time[6]
            hour = time[7]
            subprocess.call(['sudo', 'date', '-s', '{}/{}/{} {}:{}:{}'.format(year, month, day, hour, minute, s)])
            #subprocess.call(['date'])
            return
        

if __name__ == "__main__":
    dateTime()
