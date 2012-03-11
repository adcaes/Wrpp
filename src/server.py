from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

from app import App

class ServerTop(Resource):
	def __init__(self, app):
		Resource.__init__(self)
		self.app = app
		self.form = open('/home/adria/Wrpp/views/base.html', 'r').read()

	def render_GET(self, request):
		return self.form

	def getChild(self, path, request):
		if path == '':
			return self
		elif path == '_shorten':
			return ServerShorten(self.app)
		#return Resource.getChild(self, name, request)
		else:
			return ServerRedirect(self.app, path)

class ServerShorten(Resource):
	isLeaf = True
	def __init__(self, app):
		Resource.__init__(self)
		self.app = app
		self.form = open('/home/adria/Wrpp/views/base.html', 'r').read()

	def render_POST(self, request):
		return self.app.get_short_url(request.args['url'][0])
		
class ServerRedirect(Resource):
	isLeaf = True
	def __init__(self, app, path):
		Resource.__init__(self)
		self.app = app
		self.path = path
		self.form = open('/home/adria/Wrpp/views/base.html', 'r').read()

	def render_GET(self, request):
		print "path" + self.path
		return self.app.get_long_url(self.path)


app = App()

root = ServerTop(app)
#shorten = ServerShorten(app)
#resolve = ServerRedirect(app)

#root.putChild('#shorten', shorten)
#root.putChild('#shorten', resolve)

factory = Site(root)
reactor.listenTCP(8080, factory)
reactor.run()
