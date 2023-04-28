import requests
import dailyindicators, realtime
import pandas as pd

df = pd.read_excel("stocks.xlsx")
stocks = []
for i in range(len(df)):
    stock = {"symbol": df.iloc[i]["symbol"], "name": df.iloc[i]["name"]}
    stocks.append(stock)

for stock in stocks:
    symbol = stock["symbol"] + ".NS"
    name = stock["name"]
    recommendation = 0
    msg = ""
    print(" ")
    print("Checking: " + symbol)
    print(name)
    # symbol = "HPAL.NS"
    period = "50"
    sma50 = dailyindicators.getsma(symbol, period)
    ema50 = dailyindicators.getema(symbol, period)
    price, previousClose = realtime.getprice(symbol)
    if price > sma50 > previousClose:
        print(name)
        print("BUY")
        recommendation = 1
        msg = f"{name}\nPrice: {price}\nClosing Price: {previousClose}\nSMA50: {sma50}\nRecommendation: BUY (SMA Crossover)"
        base_url = 'https://api.telegram.org/bot1796740053:AAG61ntffQnu9rV_qtoD5wWeA7poXJ2f8bk/sendMessage?chat_id' \
                   '=-578120624&text="{}"'.format(msg)
        requests.get(base_url)

    if price < sma50 < previousClose:
        print(name)
        print("SELL")
        recommendation = 1
        msg = f"{name}\nPrice: {price}\nClosing Price: {previousClose}\nSMA50: {sma50}\nRecommendation: SELL (SMA Crossover)"
        base_url = 'https://api.telegram.org/bot1796740053:AAG61ntffQnu9rV_qtoD5wWeA7poXJ2f8bk/sendMessage?chat_id' \
                   '=-578120624&text="{}"'.format(msg)
        requests.get(base_url)

    if price > ema50 > previousClose:
        print(name)
        print("BUY")
        recommendation = 1
        msg = f"{name}\nPrice: {price}\nClosing Price: {previousClose}\nSMA50: {ema50}\nRecommendation: BUY (EMA Crossover)"
        base_url = 'https://api.telegram.org/bot1796740053:AAG61ntffQnu9rV_qtoD5wWeA7poXJ2f8bk/sendMessage?chat_id' \
                   '=-578120624&text="{}"'.format(msg)
        requests.get(base_url)

    if price < ema50 < previousClose:
        print(name)
        print("SELL")
        recommendation = 1
        msg = f"{name}\nPrice: {price}\nClosing Price: {previousClose}\nSMA50: {ema50}\nRecommendation: SELL (EMA Crossover)"
        base_url = 'https://api.telegram.org/bot1796740053:AAG61ntffQnu9rV_qtoD5wWeA7poXJ2f8bk/sendMessage?chat_id' \
                   '=-578120624&text="{}"'.format(msg)
        requests.get(base_url)
