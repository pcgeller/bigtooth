import RPi.GPIO as GPIO
import time

class statusLight:
    def ___init__(self, name, gpio):
        self.name = name
        self.gpio = gpio
        GPIO.setmode(GPIO.BMC)
        GPIO.setwarnings(False)
        GPIO.setup(gpio, GPIO.OUT)

    def turnOn():
        GPIO.output(self.gpio, GPIO.HIGH)
        print("LED on GPIO pin %s is turned on.", %s)

    def turnOff():
        GPIO.output(self.gpio, GPIO.LOW)
        print("LED on GPIO pin %s is turned off.", %s)



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.OUT)
print("LED on")
GPIO.output(21,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(21,GPIO.LOW)

GPIO.setup(26,GPIO.OUT)
GPIO.output(26,GPIO.HIGH)
GPIO.output(21,GPIO.LOW)


GPIO.setup(20,GPIO.OUT)
GPIO.output(20,GPIO.HIGH)
GPIO.output(21,GPIO.LOW)


GPIO.cleanup()
