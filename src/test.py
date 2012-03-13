import random

from app import App
from cache import Cache, DoublyLinkedList, Node

class Test:
	def testCache(self, n):
		m = Cache(n)

		# Insert n elements, (0, n]
		for i in range(0, n):
			m.set(i, i+1)
		
		# Retrieve n elements, (0, n]
		for i in range(0, n):
			r = random.randrange(0, n)
			assert r+1 == m.get(r)
		
		# Insert n elements, (n, n+n]
		for i in range(n, n+n):
			m.set(i, i+1)
		
		# Retrieve n elements, (n, n+n]
		for i in range(0, n):
			r = random.randrange(n, n+n)
			assert r+1 == m.get(r)

		# Retrieve n elements, (0, n]
		# Elements should have been deleted from cache
		for i in range(0, n):
			assert m.get(i) == None
		
	def testApp(self, n):
		a = App(0)
		urls = {}
		
		# Shorten n/2 URLS
		for url in range(0, n/2):
			short = a.get_short_url(url)
			assert type(short) == str
			assert short[0] == '0'
			urls[short] = url
	
		# Retrive n/2 long urls from short urls
		for shortUrl in urls.iterkeys():
			assert urls[shortUrl] == a.get_long_url(shortUrl)
			
		# Shorten n/2 URLS
		for url in range(n/2, n):
			short = a.get_short_url(url)
			assert type(short) == str
			assert short[0] == '0'
			urls[short] = url
	
		# Retrive n long urls from short urls
		for shortUrl in urls.iterkeys():
			assert urls[shortUrl] == a.get_long_url(shortUrl)
			

if __name__ == "__main__":
	t = Test()
	print "Runing tests..."
	t.testCache(5000)
	t.testApp(5000)
	print "All tests passed"
