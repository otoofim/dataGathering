import can
import subprocess
import datetime

def dateTime():
    can_interface = 'can0'
    bus = can.interface.Bus(can_interface, bustype='socketcan')

    while True:
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
            return
            #return [day, month, year, hour, minute, s]
        print('Waiting for CAN BUS')

if __name__ == "__main__":
    dateTime()
