import sys
sys.path.insert(0, '/home/pcgeller/bigtooth/')

lights = [('bigtooth', 21), ('blueHydra', 26), ('extra', 20)]
lights["blueHydra":21]

light = statusLight("blueHydra", 21)
light.turnOn()
light.turnOff()
blueHydraLED = statusLight("blueHydra", 21)
gpsLED = statusLight("GPS",26)

blueHydraLED.turnOn()
gpsLED.turnOn()
