import memcache
import urlparse

from config import *
from cache import Cache

class App:

	def __init__(self):
		self.db = memcache.Client([DB_ADDRESS], debug=0)
		self.cache = Cache(CACHE_ENTRIES)
		self.nextCodeCount = self._get_code_count()
		
	def get_short_url(self, longUrl):
		code = self._get_next_code()
		self.db.set(code, longUrl)
		self.db.set("_nextCodeCount", self.nextCodeCount)
		return "Short URL: " + APP_URL + code
			
	def get_long_url(self, shortUrl):
		longUrl = self.cache.get(shortUrl)
		if not longUrl:
			longUrl = self.db.get(shortUrl)
			if longUrl:
				self.cache.set(shortUrl, longUrl)
		return longUrl
	
	def _get_code_count(self):
		lastCodeCount = self.db.get("_nextCodeCount")
		if lastCodeCount:
			return lastCodeCount
		else:
			return 0
	
	def _get_next_code(self):
		code = self._alphabet_encode(self.nextCodeCount)
		self.nextCodeCount += 1
		return code
		
	def _alphabet_encode(self, num):
		# Special case for zero
		if num == 0:
		    return ALPHABET[0]
	 
		code = ''
	 
		while num != 0:
		    num, i = divmod(num, len(ALPHABET))
		    code = ALPHABET[i] + code
	 
		return code
