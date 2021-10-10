import requests
import json


def decode(data):
    data = list(data)
    for i in range(len(data)):
        data[i] = data[i] - 21
        data[i] = chr(data[i] - ((i - 14) % 6))
    return ''.join(data)


data = requests.get(
    'https://priority-static-api.nkstatic.com/storage/static/multi?appid=11&files=races/Exponential_4')
buffer = data.content
decoded = decode(buffer)
obj = json.loads(decoded)
print(obj)
