#!/usr/bin/env python

import time
import serial

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 19200,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0

while 1:
    x=ser.read(32)
    print(x)
