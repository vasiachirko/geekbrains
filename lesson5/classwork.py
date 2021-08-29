import json

py = {}
py['xxx'] = 'yyy'

with open('json.txt', 'r') as fp:
    print(json.load(fp))