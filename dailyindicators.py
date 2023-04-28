import requests


def getsma(symbol, period):
    url = 'https://fmpcloud.io/api/v3/technical_indicator/daily/' + symbol + '?period=' + period + '&type=sma&apikey=API-KEY'
    r = requests.get(url)
    data = r.json()
    # print(data)
    for smaData in data:
        sma = smaData["sma"]
        # closeprice = smaData["close"]
        break
    if not data:
        sma = 0
    return sma


def getema(symbol, period):
    url = 'https://fmpcloud.io/api/v3/technical_indicator/daily/' + symbol + '?period=' + period + '&type=ema&apikey=API-KEY'
    r = requests.get(url)
    data = r.json()
    # print(data)
    for emaData in data:
        ema = emaData["ema"]
        # closeprice = smaData["close"]
        break
    if not data:
        ema = 0
    return ema
