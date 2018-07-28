import serial
from time import sleep
import os
import re

modem = serial.Serial("/dev/ttyUSB2", baudrate=115200 ,bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=1, dsrdtr=1)
f = open("gsm.log","a")
while True:
    raw = modem.readline().decode('utf-8')
    # print(raw)
    d = raw.split('\r\n')
    s= d[0]
    t = s
    print(t)

    if '+CMTI: "SM",' in t:
        print("Received new message")
        r = s.split(',')
        rxSMSnum = r[1]
        print("Message location :" + rxSMSnum)
    
    if '+CLIP:' in t:
        print("Incoming Call")
        r = s.split(',')
        rxCALLnum = r[0]
        # re.search('[1-9][0-9]*',a).group()

        fd = re.search('[1-9][0-9]*',rxCALLnum).group()
        # pat = re.compile(r'"*"')
        # mat = pat.finditer(rxCALLnum)
        print("Message location :" '{}'.format(fd))
        # print(r[2])
    # pattern = re.compile(r'+CMTI:')
    # matches = pattern.finditer(raw)
    # print(matches)
    # for match in matches:
    #     print(match)
#     f.write(raw)
#     k = t.strip()
#     print(k) 
#     if d[0]=='+CMTI: "SM",20':
#         print("gotcha")
# f.close()

"""
+CMTI: "SM",0
AT+CMGR=0
+CMGR: "REC UNREAD","+9607991206",,"18/07/28,12:24:58+20"
"""