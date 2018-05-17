import serial

ser = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=2.0)
ser.write('AT\r')
print ser("AT Command was Sent.\n waiting for OK\n")
print ser.read(100) #if everything went as expected it should return OK
ser.close()
