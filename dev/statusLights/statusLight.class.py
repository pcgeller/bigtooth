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
