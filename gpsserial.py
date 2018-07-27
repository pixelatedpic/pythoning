import serial
from time import sleep
from decimal import *

gpsport = serial.Serial("/dev/ttyAMA0",baudrate=115200 ,bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)

def dm(x):
    degrees = int(x) // 100
    minutes = x - 100*degrees
    #print(degrees)
    #print(minutes)
    conval =  degrees + minutes/60
    conval = '{0:.6f}'.format(round(conval,6))
#    print(conval,6)
    return conval
#gpsport.flush()
#sleep(5)
while True:
	try:
	#	sleep(.5)
	#	gpsport.flush()
		raw = gpsport.readline()
		# print(raw)

		# if raw != 0xff or 0xf0 or 0xac or 0xa7:
		rxgps = raw.decode('utf-8')[:-1]
#		else:
#			rxgps = ""
	#	rxgps = gpsport.readline().decode('utf-8')[:-1]
		#rxgps = gpsport.readline()
		#line = .decode('utf-8')[:-1]
		data = rxgps.split(',')
		#print(data[1])
	#	print(rxgps)
		if data[0] == "$GPGGA":
			print(rxgps)
	#		print(data[1])
			UTCtime = data[1]
			Latitude = data[2]
			Longitude = data[4]
			SAT = data[7]
			FIX = data[6]
#			print(Latitude)
			decLat = Decimal(Latitude)
			decLon = Decimal(Longitude)
#			f = str(Latitude)
#			print(f)
			bapLat=dm(decLat)
			bapLon=dm(decLon)

			print("UTC: " + UTCtime)
			print("SAT: " + SAT)
			print("FIX: " + FIX)
			print("LAT: " '{}'.format(bapLat))
			print("LON: " '{}'.format(bapLon))
			
	except KeyboardInterrupt:
		print('Program stoped by the master')
		gpsport.close()
		break
		#raise
