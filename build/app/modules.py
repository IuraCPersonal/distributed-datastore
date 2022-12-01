import os
import json

NAME = os.getenv('NAME')

def read_json(file):
    current_directory = os.getcwd()
    with open(f'.{current_directory}/data/{file}', 'r') as f:
        data = json.load(f)

    return data

CLUSTER = read_json('cluster.json')
SERVER_DATA = CLUSTER[NAME]
SERVERS_LIST = ['alpha', 'beta', 'gamma', 'delta']

datastore = dict()
