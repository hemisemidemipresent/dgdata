import requests


def decode(data):

    protoBuff = []

    for i in range(len(data)):
        protoBuff.append(data[i])

    for i in range(len(protoBuff)):
        protoBuff[i] = protoBuff[i] - 21
        protoBuff[i] = protoBuff[i] - ((i - 14) % 6)
    res = ''
    for i in range(len(protoBuff)):
        res += chr(protoBuff[i])
    return res


data = requests.get(
    'https://priority-static-api.nkstatic.com/storage/static/multi?appid=11&files=races/Exponential_4')
print(data.content)
print(decode(data.content))
