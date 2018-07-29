import serial
from time import sleep
import os
import re
# import threading
# from queue import queue
# import time


modem = serial.Serial("/dev/ttyUSB2", baudrate=115200 ,bytesize=8, parity='N', stopbits=1, timeout=5, xonxoff=0, rtscts=1, dsrdtr=1)
f = open("gsm.log","a")
# modem.write(b'AT+CMGF=1\r')

def readmsg(x):
    readData = ['']
    modem.write(b'AT+CMGR='+ x.encode() + b'\r')
    modem.flush()
    while True:
        size = modem.inWaiting()
        if size:
            readData[0] = modem.read(size).decode('utf-8')
            # print(readData[0])
            if 'OK' in readData[0]:
                modem.write(b'AT+CMGD='+ x.encode() + b'\r')
                # sleep(.5)
                return readData[0].strip('\r\n')
        # else:
        #     return readData[0]
        #     break

        # readData[0] = modem.readline().decode('utf-8')
        # # print(readData)
        # if '+CMGR: "REC READ"' in readData[0]:
        #     print(readData)
            # readData[0] = modem.readline().decode('utf-8')
            
            # if 'OK' in readData[0]:
            #     print(readData)
                # return readData[0]
        



# (self, parameter_list):        

#     pass
# while True:
#     readData = modem.readline().decode('utf-8')
# # if readData !="":
#     chopData = readData
# # print(chopData)

# # a = chopData.split("\r\r\n")
# a = chopData.split("\r\n")
# # print(a)
# rxSMSnum='0'
# modem.write(b'AT+CMGR='+ rxSMSnum.encode() + b'\r')
# print(chopData)

x = "0"
f = readmsg(x)
# modem.write(b'AT+CMGD='+ x.encode() + b'\r')
# c = f.strip('\r\n')
# sleep(1)
# print(f)
if '+CMGR:' in f:

    cc = re.search('[1-9][0-9]*',f).group()
    cd = re.search('\"+[1-9][0-9].+\"',f).group()
    
    # print("Message location :" '{}'.format(cc))
    # msgnumber = f[23:30].strip()
    msgcont = f[55:-2].strip()
    msgcont = msgcont
    print("Message timestamp: "'{}'.format(cd))
    print("Message number: "'{}'.format(cc))
    print("Message: "+msgcont)


# while True:








# while True:
#     rxSMSnum = ""
#     readData = modem.readline().decode('utf-8')

#     # if readData !="":
#     chopData = readData
#     # print(chopData)

#     # a = chopData.split("\r\r\n")
#     a = chopData.split("\r\n")
#     # print(a)
#     rxSMSnum='0'
#     modem.write(b'AT+CMGR='+ rxSMSnum.encode() + b'\r')
#     print(chopData)

    # print("data in a: '{}' ".format(a[0]))
    # if '+CLIP:' in a[0]:
    #     print("----Incoming Call----")
    #     rawClip = a[0].split(',')
    #     rxCALLnum = rawClip[0]
    #     rxCID = re.search('[1-9][0-9]*',rxCALLnum).group()
    #     print("Caller ID: "'{}'.format(rxCID))

    # if '+CMTI: "SM",' in a[0]:
    #     print("Received new message")
    #     rawSplit = a[0].split(',')
    #     rxSMSnum = rawSplit[1]
    #     print("Message id: " + rxSMSnum)
    
    # if rxSMSnum !="":
    #     print("Read MSG")
    #     modem.write(b'AT+CMGR='+ rxSMSnum.encode() + b'\r')
    #     modem.flush()
    #     modem.flush()
    #     modem.flush()
    #     modem.flush()
    #     modem.flush()
    #     modem.flush()
    #     # while 1:
    #     # sleep(1)
    #     chopData = modem.readline().decode('utf-8')
    #     amsg = chopData.split("\r\n")
    #     if chopData !="":
    #         print(amsg)
    #         if '+CMGR: "REC UNREAD"' in amsg[0]:
    #             print("reading msamsgg")
    #             rawSplit = amsg[0].split(',')
    #             # rawSplit = amsg[0].strip(' ')
    #             cid = rawSplit[1]
    #             td = rawSplit[3]
    #             td += rawSplit[4]
    #             print(cid)
    #             print(td)
    #             print(rawSplit)
    #                 # break
# +CMGR: "REC UNREAD","+9607991206",,"18/07/29,18:30:45+20"
# Yes ruffudufufug

# OK