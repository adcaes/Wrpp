from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource

class LoadBalancer(Resource):
	def __init__(self):
		Resource.__init__(self)

	def getChild(self, path, request):
		return ReverseProxyResource('localhost', 8888, "/"+path)


root = LoadBalancer()

factory = Site(root)
reactor.listenTCP(8080, factory)
reactor.run()
