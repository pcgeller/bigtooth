import sys

sys.path.insert(0, '/home/pcgeller/bigtooth/dev/statusLights')
sys.path.insert(0, '/home/pi/bigtooth/dev/statusLights')
import statusLightClass as sl
lightConfig = {'bigtooth': 21, 'blueHydra': 26, 'extra': 20}
#lights["blueHydra":21]

def initLights(config):
    lights = {}
    for name, gpio in config.items():
        print('%s %s' % (name, gpio))
        light = sl.statusLight(name, gpio)
        print(light)
        lights[light.name] = light

    return(lights)



lights = initLights(lightConfig)

light = sl.statusLight("blueHydraLED", 21)
light = sl.statusLight("blueHydra", 21)
light.turnOn()
light.turnOff()
blueHydraLED = sl.statusLight("blueHydra", 21)
gpsLED = sl.statusLight("GPS",26)

blueHydraLED.turnOn()
gpsLED.turnOn()
