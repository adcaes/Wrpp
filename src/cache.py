# Least Recently Used (LRU) Cache implementation

class Node:
	def __init__(self, data = None):
		self.prev = None
		self.next = None
		self.data = data
		
class DoublyLinkedList:
	def __init__(self):
		self.root = Node("ROOT")
		self.root.prev = self.root  #tail
		self.root.next = self.root  #head

	def insertHead(self, newNode):
		newNode.next = self.root.next
		newNode.prev = self.root
		newNode.next.prev = newNode
		newNode.prev.next = newNode
		
	def moveToHead(self, node):
		self.remove(node)
		self.insertHead(node)

	def removeLast(self):
		n = self.root.prev
		self.list.remove(n)
		return n.data
	
	def remove(self, node):
		node.next.prev = node.prev
		node.prev.netx = node.next

class Cache:
	def __init__(self, maxSize=1000):
		self.index = {}
		self.list = DoublyLinkedList()
		self.maxSize = maxSize
		self.size = 0
	
	# Adds a (value, key) pair to the cache
	# If the cache is full the least recently used element is deleted
	def set(self, key, value):
		if self.size > self.maxSize:
			(key, value) = self.list.removeLast()
			del self.index[key]
		else:
			self.size += 1
			
		node = Node((key, value))
		self.list.insertHead(node)
		self.index[key] = node		
	
	# Gets the value associtaed with key from the cache
	# Returns None if the key is not present	
	def get(self, key):
		if key in self.index:
			node = self.index[key]
			self.list.moveToHead(node)
			return node.data[1]
		else:
			return None



