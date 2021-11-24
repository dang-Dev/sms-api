import serial
import RPi.GPIO as GPIO
import time, os, sys

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

port.write(b'AT\r\n')
rcv = port.read(50)
#print(rcv.decode("utf-8"))
time.sleep(.1)

#port.write(b'ATEO\r\n')
#rcv = port.read(50)
#print(rcv.decode("utf-8"))
#time.sleep(.1)

#Select Message format as text mode
port.write(b'AT+CMGF=1\r\n')
rcv = port.read(50)
#print(rcv.decode("utf-8"))
time.sleep(.1)

#New Message Indications
#port.write(b'AT+CNMI=2,1,0,0,0\r\n')
#rcv = port.read(50)
#print(rcv.decode("utf-8"))
time.sleep(.1)

#sending a message to particular number
contact_num = 'AT+CMGS="'+ str(sys.argv[1]) +'"\r\n'
b_mess = contact_num.encode("utf-8")
port.write(b_mess)
rcv = port.read(50)
#print(rcv.decode("utf-8"))
time.sleep(.1)

#message
message = str(sys.argv[2]) + '\r\n'
#print(message)
message = message.replace("%", " ")
#message = "ako lang to"
port.write(message.encode("utf-8"))
rcv = port.read(50)
#print(rcv.decode("utf-8"))

#enable to send sms
port.write(b'\x1A')
#for i in range(10):
#    rcv = port.read(10)
#    print(rcv.decode("utf-8"))
time.sleep(1)
