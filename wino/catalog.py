from base import Base

class Catalog(Base):
	def __init__(self, apikey):
		Base.__init__(self, apikey)
		self.url = "/".join((self.ENDPOINT, "catalog"))

	def search(self, string, **params):
		payload = dict( params.items() + { 'search': string }.items())
		json = self.get(self.url, params=payload)
		return json['Products']['List']