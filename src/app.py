import memcache
import urlparse

from config import *
from cache import Cache

class App:

	def __init__(self, serverId):
		# Open DB connection
		self.db = memcache.Client([DB_ADDRESS[serverId]], debug=0)
		# Initialize cache
		self.cache = Cache(MAX_CACHE_ENTRIES)
		# Initialize the nextCodeCount, used to generate short URLs
		self.nextCodeCount = self._get_code_count()
		# Prefix used by this app instance when generating URLs
		self.prefix = PREFIXES[serverId]
		
	def get_short_url(self, longUrl):
		# Generate a code for the URL
		code = self.prefix + self._get_next_code()
		# Store in the DB the mapping between the URL and the code
		self.db.set(code, longUrl)
		return code
			
	def get_long_url(self, shortUrl):
		# Try to get original URL from Cache
		longUrl = self.cache.get(shortUrl)
		if not longUrl:
			# If not in cache, get it from DB
			longUrl = self.db.get(shortUrl)
			if longUrl:
				# Add the retreived URL to the cache
				self.cache.set(shortUrl, longUrl)
		return longUrl
	
	def _get_code_count(self):
		# Fetch from DB the stored value for nextCodeCount
		lastCodeCount = self.db.get("_nextCodeCount")
		if lastCodeCount:
			return lastCodeCount
		else:
			# If it is not in DB, start it to 0
			return 0
	
	def _get_next_code(self):
		# Get code from nextCodeCount
		code = self._alphabet_encode(self.nextCodeCount)
		# Update nextCodeCount
		self.nextCodeCount += 1
		# Update nextCodeCount, used when the app is restarted
		self.db.set("_nextCodeCount", self.nextCodeCount)
		return code

	
	def _alphabet_encode(self, num):
		# Special case for zero
		if num == 0:
		    return ALPHABET[0]
	 
		code = ''
	 
		while num != 0:
		    num, i = divmod(num, len(ALPHABET))
		    code = ALPHABET[i] + code
	 	
	 	# Return nextCodeCount represented with ALPHABET
		return code
