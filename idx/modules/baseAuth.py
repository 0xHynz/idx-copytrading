"""
this auth program recode from https://
"""


import requests
import time
import hashlib
import hmac
from urllib.parse import urlencode
import key


class auth():
    def __init__(self,key,sign):
        self.key = key
        self.sign = sign

    def __call__(self, r):
        r.headers['Key'] = self.key
        r.headers['Sign'] = self.sign
        return r

def nonce():
    time.sleep(1/1000)
    return str(int(time.time()*1000))

def signature(secret, params):
    sig = hmac.new(secret.encode(), params.encode(), hashlib.sha512)
    return sig.hexdigest()


class API:
    def __init__(self, key=key.API, secret=key.SECRET):
        self.__key = key
        self.__secret = secret

    def callFunction(self, method,params):
        self.url = 'https://indodax.com/tapi'
        self.params = params; self.params['method'] = method; self.params['nonce'] = nonce()

        self.authData = auth(self.__key, signature(self.__secret, urlencode(self.params)))
        self.r = requests.Session()
        self.rdata = self.r.post(self.url, data=self.params, auth=self.authData)
        return self.rdata



