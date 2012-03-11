from config import *
import memcache
import cache

class App:

	def __init__(self):
		self.db = memcache.Client([DB_ADDRESS], debug=0)
		self.cache = Memcache() 
		self.nextCode = 0
		
	def get_short_url(self, longUrl):
		code = self._get_next_code()
		db.set(code, longUrl)
		return code
			
	def get_long_url(self, shortUrl):
		longUrl = self.cache.get(shortUrl)
		if not longUrl:
			longUrl = self.db.get(shortUrl)
		
		return longUrl
	
	
	def _get_next_code(self):
		code = self._alphabet_encode(self.nextCode)
		self.nextCode += 1
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
		
a = App()
urls = []
for i in range(900, 1000, 1):
	urls.append(a.get_short_url(i))
	print urls[-1]
	
print "DECODING"
	
for i in range(0, 100, 1):
	print a.get_long_url(urls[i])
