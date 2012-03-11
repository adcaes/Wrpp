from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource

from config import *

class LoadBalancer(Resource):
	def __init__(self):
		Resource.__init__(self)
		# Id of the next server to use
		self.serverPointer = 0
		
	def getChild(self, path, request):
		server = self._getServer(path)
		return ReverseProxyResource('localhost', server, "/"+path)

	# Return the App server where the request has to be redirected
	def _getServer(self, path):
		print "get server " + path
		if path == '' or path == '_shorten':
			self.serverPointer = (self.serverPointer + 1)%len(SERVERS)
			return SERVERS[self.serverPointer]
		else:
			if PREFIXES.count(path[0]) > 0:
				pos = PREFIXES.index(path[0])
				return SERVERS[pos]
			else:
				print "Load Balancer: Not found prefix: " + path[0]
				return SERVERS[0]
				
if __name__ == "__main__":
	root = LoadBalancer()

	factory = Site(root)
	reactor.listenTCP(8080, factory)
	reactor.run()
