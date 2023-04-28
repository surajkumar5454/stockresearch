import requests


def getprice(symbol):
    url = 'https://fmpcloud.io/api/v3/quote/' + symbol + '?apikey=API-KEY'
    r = requests.get(url)
    data = r.json()
    # print(data)
    price, previousClose = "", ""
    for pricedata in data:
        price = pricedata["price"]
        previousClose = pricedata["previousClose"]
    if not data:
        price = 0
        previousClose = 0

    return price, previousClose
