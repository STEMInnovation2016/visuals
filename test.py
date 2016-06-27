#copy and paste into the command line of the pi to open the visual stream
#make sure to use the IP address of the Pi

raspivid -t 999999 -h 720 -w 1080 -fps 25 -b 2000000 -o - | gst-launch-1.0 -v fdsrc ! h264parse !  rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.2.116 port=5000

#install gstreamer onto the receiving computer
#copy and paste into the command line
#make sure to use the IP address of the Pi
#gst-launch-1.0 -v tcpclientsrc host=YOUR-PI-IP-ADDRESS port=5000  ! gdpdepay !  rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false