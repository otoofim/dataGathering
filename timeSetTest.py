import time
import can

bustype = 'socketcan'
channel = 'can0'


bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = can.Message(arbitration_id=1536, data=[11,20,5,30,43,59,20,9], is_extended_id=False)
bus.send(msg)




