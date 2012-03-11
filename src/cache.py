
class Node:
	def __init__(self, data = None):
		self.prev = None
		self.next = None
		self.data = data
		
class DoublyLinkedList:
	def __init__(self):
		self.root = Node("ROOT")
		self.root.prev = self.root  #head
		self.root.next = self.root  #tail
		self.size = 0

	def insertHead(self, newNode):
		newNode.next = self.root.next
		newNode.prev = self.root
		newNode.next.prev = newNode
		newNode.prev.next = newNode

	def moveToHead(self, node):
		self.remove(node)
		self.insertHead(node)
		
	def remove(self, node):
		node.next.prev = node.prev
		node.prev.netx = node.next

class Memcached:
	def __init__(self):
		self.index = {}
		self.list = DoublyLinkedList() 
		
	def set(self, key, value):
		node = Node(value)
		self.list.insertHead(node)
		self.index[key] = node		
		
	def get(self, key):
		if key in self.index:
			node = self.index[key]
			self.list.moveToHead(node)
			return node.data
		else:
			return None
		
		
m = Memcached()

for i in range(900, 1000, 1):
	m.set(i, i)
	
print "DECODING"
	
for i in range(999, 899, -1):
	a = m.get(i)
	print str(a) + " " + str(i)


