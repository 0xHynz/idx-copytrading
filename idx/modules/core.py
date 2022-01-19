import requests
import json
from baseAuth import API 


class Instruction:

     def __init__(self):
         self.call = API()

     @staticmethod
     def getBestPositionToBuy(data):
         return {'area':int(data['price'])+1}

     def orderbooks_analysis(self,coin):
         self.transaction = json.loads(self.call.callFunction('tradeHistory',{'pair':coin}).text)
         self.buyer, self.seller = [],[]
         self.data = self.transaction['return']['trades']

         for _ in self.data:
             if _['type'] == 'buy':
                self.buyer.append(_)
             else:
                self.seller.append(_)


         highBuyer,highSeller = [],[]

         for _ in self.buyer:
             highBuyer.append(_['vra'])
         for _ in self.seller:
             highSeller.append(_['vra'])

         if max(highBuyer) >= max(highSeller):
            buyerInfo = {}
            for _ in self.data:
                if _['vra'] == max(highBuyer):
                   buyerInfo = _
            print('Buy in ',Instruction.getBestPositionToBuy(buyerInfo))



y = Instruction()
y.orderbooks_analysis('vra_idr')
