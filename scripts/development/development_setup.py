import json
from pprint import pprint

with open('config_dev.json') as config_file:
    data = json.load(config_file)

pprint(config_file)
