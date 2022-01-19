import requests
import json


class indodaxApi:

    def __init__(self):
        self.apiPath = "https://indodax.com/api/"

    def getTickers(self):
        self.reqs = requests.get(self.apiPath+'tickers').text
        return self.reqs

    def altCoinlist(self):
        self.tickersRes = json.loads(self.getTickers())['tickers']
        self.coinName = []
        for c in self.tickersRes:
            self.coinName.append(c)

        return self.tickersRes




