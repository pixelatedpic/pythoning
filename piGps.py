import serial
from time import sleep

gpsport = serial.Serial("/dev/ttyAMA0",bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
#gpsport.flush()
#sleep(5)
while True:
#       sleep(.5)
#       gpsport.flush()
        raw = gpsport.readline()
#       print(raw)
        if raw != 0xff:
                rxgps = raw.decode('utf-8')[:-1]
        else:
                rxgps = ""
#       rxgps = gpsport.readline().decode('utf-8')[:-1]
        #rxgps = gpsport.readline()
        #line = .decode('utf-8')[:-1]
        data = rxgps.split(',')
        #print(data[1])
#       print(rxgps)
        if data[0] == "$GPGGA":
                print(rxgps)
#               print(data[1])
                UTCtime = data[1]
                Latitude = data[2]
                Longitude = data[4]
                SAT = data[7]
                FIX = data[6]

                print("UTC: " + UTCtime)
                print("SAT: " + SAT)
                print("FIX: " + FIX)
                print("LAT: " + Latitude)
                print("LON: " + Longitude)

gpsport.close()
