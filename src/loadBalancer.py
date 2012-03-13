from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource

from config import *
from myLogger import *

class LoadBalancer(Resource):
	def __init__(self):
		Resource.__init__(self)
		# Id of the next server to use
		self.serverPointer = 0
		# Logger used for logging
		self.logger = loggerInit('loadBalancer')
		
	def getChild(self, path, request):
		serverId = self._getServer(path)
		self.logger.info('Received request with path: ' + path + ' forwading to serverId: ' + str(serverId))
		# Forward request to the selected server
		return ReverseProxyResource(SERVERS[serverId][HOST], SERVERS[serverId][PORT], "/"+path)

	# Return the App server where the request has to be redirected
	def _getServer(self, path):
		if path == '' or path == '_shorten' or (not PREFIXES.count(path[0])):
			self.serverPointer = (self.serverPointer + 1)%len(SERVERS)
			return self.serverPointer
		else:
			# Request redirect given short URL with valid prefix
			# Return serverId that handles the requested short url
			pos = PREFIXES.index(path[0])
			return pos
				
if __name__ == "__main__":
	root = LoadBalancer()
	factory = Site(root)
	reactor.listenTCP(LOAD_BALANCER_PORT, factory)
	reactor.run()
