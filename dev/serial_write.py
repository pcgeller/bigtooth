import time
import serial

ser = serial.Serial(
    port = '/dev/ttyS0',
    baudrate = 19200,
   # parity=serial.parity.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

counter = 0
while True:
    #s = 'Write counter: %d'%(counter)
    prompt = input("Enter AT command:")
    promptInBytes = str.encode(s)
    ser.write(promptInBytes)
    time.sleep(1)
    counter += 1
