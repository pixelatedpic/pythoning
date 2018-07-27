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
		#reading the serial port , decode and remove the line terminations
		raw = gpsport.readline().decode('utf-8')[:-1]
		#print(raw)
		data = raw.split(',')
		#print(data[2])
		if data[0]== "$GPRMC":
			if data[2] !="V":
#				print(raw)
				UTCtime = data[1]
				Latitude = data[3]
				Longitude = data[5]
				# print(Latitude)
				# print(Longitude)
				decLat = Decimal(Latitude)
				decLon = Decimal(Longitude)
				bapLat=dm(decLat)
				bapLon=dm(decLon)
				print("UTC: " + UTCtime)
				print("LAT: " '{}'.format(bapLat))
				print("LON: " '{}'.format(bapLon))

		if data[0]== "$GPGGA":
			SAT = data[7]
			FIX = data[6]
			print("SAT: " + SAT)
			print("FIX: " + FIX)

		# print("UTC: " + UTCtime)
		# print("SAT: " + SAT)
		# print("FIX: " + FIX)
		# print("LAT: " '{}'.format(bapLat))
		# print("LON: " '{}'.format(bapLon))
				
	except KeyboardInterrupt:
		print('Program stoped by the master')
		gpsport.close()
		break
