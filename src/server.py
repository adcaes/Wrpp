import sys
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

from app import App
from config import *

class ServerTop(Resource):
	def __init__(self, serverId=0):
		Resource.__init__(self)
		self.app = App(serverId)
		self.serverShorten = ServerShorten(self.app)
		self.serverRedirect = ServerRedirect(self.app)
		self.formHtml = open(APP_TOP_DIR + 'views/base.html', 'r').read()

	def render_GET(self, request):
		# Return the form to introduce a URL 
		return self.formHtml

	def getChild(self, path, request):
		if path == '':
			return self
		elif path == '_shorten':
			return self.serverShorten
		else:
			self.serverRedirect.setPath(path)
			return self.serverRedirect

class ServerShorten(Resource):
	isLeaf = True
	def __init__(self, app):
		Resource.__init__(self)
		self.app = app
		self.shortUrlHtml = open(APP_TOP_DIR + 'views/shortUrl.html', 'r').read()

	def render_POST(self, request):
		print "longURL " + request.args['url'][0]
		# Generate a code for the given URL and stores the mapping
		url = APP_URL + self.app.get_short_url(request.args['url'][0])
		# Return the short URL
		return self.shortUrlHtml % (url, url)
		
class ServerRedirect(Resource):
	isLeaf = True
	def __init__(self, app):
		Resource.__init__(self)
		self.app = app
		self.redirectHtml = open(APP_TOP_DIR + 'views/redirect.html', 'r').read()
		self.notFoundHtml = open(APP_TOP_DIR + 'views/notFound.html', 'r').read()
	
	def setPath(self, path):
		self.path = path
	
	def render_GET(self, request):
		print "Enter redirect, path= " + self.path
		# Fetch original URL from URL code
		longUrl = self.app.get_long_url(self.path)
		if longUrl:
			# Return original URL
			print "longUrl " + longUrl
			return self.redirectHtml % longUrl
		else:
			#URL Code not found
			print "ERROR: URL code " + self.path + " not found."
			return self.notFoundHtml % (APP_URL + self.path)


if __name__ == "__main__":
	serverId = int(sys.argv[1])	
	root = ServerTop(serverId)
	factory = Site(root)
	reactor.listenTCP(SERVERS[serverId], factory)
	reactor.run()

