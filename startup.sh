sudo mount /dev/sda1 /home/pi/ssd
sudo /sbin/ip link set can0 up type can bitrate 500000 loopback on

exit 0
