simport yaml

path = '/home/pcgeller/bigtooth/config.yml'
file = open(path, 'r')

with open(path, 'r') as infile:
    config = yaml.load(infile)

print(config)
