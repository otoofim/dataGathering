sudo mount /dev/sda1 /home/pi/ssd
sudo /sbin/ip link set can0 up type can bitrate 500000 loopback on

#loopback test
#coment the two following lines for deployment
/home/pi/.pyenv/versions/data_gathering/bin/python /home/pi/camera/PiCANRec.py &
/home/pi/.pyenv/versions/data_gathering/bin/python /home/pi/camera/timeSetTest.py


exit 0