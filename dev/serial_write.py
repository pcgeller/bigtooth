import time
import serial

ser = serial.Serial(
    port = '/dev/ttyS0',
    baudrate = 9600,
   # parity=serial.parity.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

counter = 0
while 1:
    s = 'Write counter: %d'%(counter)
    sb = str.encode(s)
    ser.write()
    time.sleep(1)
    counter += 1
