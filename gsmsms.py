import serial
from time import sleep
import os
import re

modem = serial.Serial("/dev/ttyUSB2", baudrate=115200 ,bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=1, dsrdtr=1)
f = open("gsm.log","a")
modem.write(b'AT+CMGF=1\r')

def readModem():
    raw = modem.readline().decode('utf-8')
    return raw

def getSms():
    rxd = readModem()
    print(rxd)
    if '+CMTI: "SM",' in rxd:
        print("gotya")
        rawSplit = rxd.split(',')
        rxSMSnum = rawSplit[1]
        print("Message location :" + rxSMSnum)
        # sendCmd(rxSMSnum)
        modem.write(b'AT+CMGR='+ rxSMSnum.encode() + b'\r')
    


    # rawx = rxd.split('\r\n')
    # print("Spltited values : '{}'".format(rawx))
    # rawClean = rawx[0]
    # print(rawx)
    # if '+CMTI: "SM",' in rawClean:
    #     print("Received new message")
    #     rawSplit = rawClean.split(',')
    #     rxSMSnum = rawSplit[1]
    #     print("Message location :" + rxSMSnum)
    #     sendCmd(rxSMSnum)
        

# def sendCmd(x):
#     modem.write(b'AT+CMGR='+ x.encode() + b'\r')
#     rxds = readModem()
#     cc = rxds.split('\r\r\n')
#     print(cc[0])
#     print(cc[2])
#     print(cc[0])

    # print("read sms: "+rxdd+"---END---")
    # if '+CMGR: "REC UNREAD"' in rxdd:
    #     print("yes")


while True:
    getSms()
    #raw = modem.readline().decode('utf-8')
    # print(raw)

    # rr = re.match(r'\+([A-Z])\w+:\s\"([1-9][0-9]*)\w+\"',s).group()
    # print("Regx Capture :" '{}'.format(rr))


        # sleep(.5)
        # rawx = modem.readline()
        # print(rawx)
    
    # if '+CMGR: "REC UNREAD"' in rawClean:
    #     print("Reading message")

        # raws = modem.readline().decode('utf-8')
        # print(raws)

    # if '+CLIP:' in rawClean:
    #     print("Incoming Call")
    #     rawClip = rawClean.split(',')
    #     rxCALLnum = rawClip[0]
    #     rxCID = re.search('[1-9][0-9]*',rxCALLnum).group()
    #     print("Message location :" '{}'.format(rxCID))


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