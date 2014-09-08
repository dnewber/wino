import requests as req

class Base(object):

    ENDPOINT = 'http://services.wine.com/api/beta2/service.svc/json'

    def __init__(self, apikey):
        self.apikey = { 'apikey': apikey };

    def get(self, url, **params):
        payload  = dict(self.apikey.items() + params['params'].items())
        response = req.get(url, params=payload)
        return response.json()

    def build_payload(self, **params):
        return