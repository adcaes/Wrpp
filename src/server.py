from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

from app import App

class ServerTop(Resource):
	def __init__(self):
		Resource.__init__(self)
		self.app = App()
		self.serverShorten = ServerShorten(self.app)
		self.serverRedirect = ServerRedirect(self.app)
		self.form = open('../views/base.html', 'r').read()

	def render_GET(self, request):
		return self.form

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
		self.form = open('../views/base.html', 'r').read()

	def render_POST(self, request):
		print "longURL " + request.args['url'][0]
		return self.app.get_short_url(request.args['url'][0])
		
class ServerRedirect(Resource):
	isLeaf = True
	def __init__(self, app):
		Resource.__init__(self)
		self.app = app
		self.form1 = open('../views/redirect.html', 'r').read()
		self.form2 = open('../views/redirect2.html', 'r').read()
	
	def setPath(self, path):
		self.path = path
	
	def render_GET(self, request):
		print "Enter redirect, path= " + self.path
		longUrl = self.app.get_long_url(self.path)
		if longUrl:
			print "longUrl " + longUrl
			return self.form1 + "window.location=\"" + longUrl + "\";" + self.form2;
		else:
			print "ERROR: URL code " + self.path + " not found."
			return "ERROR: URL code " + self.path + " not found."


root = ServerTop()

factory = Site(root)
reactor.listenTCP(8888, factory)
reactor.run()
