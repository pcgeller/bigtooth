import RPi.GPIO as GPIO
import time

class statusLight:
    def __init__(self, name, gpio):
        self.name = name
        self.gpio = gpio
        import RPi.GPIO as GPIO
        import time
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(gpio, GPIO.OUT)

    def __enter__(self):
        return self

    def turnOn(self):
        GPIO.output(self.gpio, GPIO.HIGH)
        self.status = "on"
        print("LED on GPIO pin %s is turned on." % self.gpio)

    def turnOff(self):
        GPIO.output(self.gpio, GPIO.LOW)
        self.status = "off"
        print("LED on GPIO pin %s is turned off." % self.gpio)

    def __exit__(self):
        GPIO.cleanup()

lights["blueHydra":21]

light = statusLight("blueHydra", 21)
light.turnOn()
light.turnOff()
blueHydraLED = statusLight("blueHydra", 21)
gpsLED = statusLight("GPS",26)

blueHydraLED.turnOn()
gpsLED.turnOn()

connectedGPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.OUT)
print("LED on")
GPIO.output(21,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(21,GPIO.LOW)
GPIO.cleanup()
