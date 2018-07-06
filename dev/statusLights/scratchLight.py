import sys
sys.path.insert(0, '/home/pcgeller/bigtooth/dev')
import statusLight

lightConfig = {'bigtooth': 21, 'blueHydra': 26, 'extra': 20}
#lights["blueHydra":21]

def initLights(config):
    for name, gpio in config.items():
        lights = []
        light = statusLight(name, gpio)
        lights.append(light)
        




    light = statusLight("blueHydraLED", 21)
light = statusLight("blueHydra", 21)
light.turnOn()
light.turnOff()
blueHydraLED = statusLight("blueHydra", 21)
gpsLED = statusLight("GPS",26)

blueHydraLED.turnOn()
gpsLED.turnOn()
