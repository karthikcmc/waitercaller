import urllib2
import json

TOKEN = "9a4afbe7af66e87b33085bdbf5d10f14554ba28f"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:
	
	def shorten_url(self, longurl):
		try:
			url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
			response = urllib2.urlopen(url).read()
			jr = json.loads(response)
			return jr['data']['url']
		except Exception as e:
			print e
