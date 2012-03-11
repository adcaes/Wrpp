from config import *

class App:

	def __init__(self):
		self.urls = {}
		self.nextShort = 0
		
	def get_short_url(self, longUrl):
		code = self._get_next_code()
		self.urls[code] = longUrl
		return code
			
	def get_long_url(self, shortUrl):
		if shortUrl in self.urls:
			return self.urls[shortUrl] 
		else:
			return "URL Not Found"
	
	def _get_next_code(self):
		code = self._alphabet_encode(self.nextShort)
		self.nextShort += 1
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
