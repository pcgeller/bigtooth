__init__

import dbOpener

with open(config, 'r') as f:
    config = yaml.load(f)
    keys, values = zip(*config.items())

def dbList()
