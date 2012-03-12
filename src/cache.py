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
		self.root.next = newNode
		
	def moveToHead(self, node):
		self.remove(node)
		self.insertHead(node)

	def removeLast(self):
		n = self.root.prev
		self.remove(n)
		return n.data
	
	def remove(self, node):
		node.next.prev = node.prev
		node.prev.next = node.next
	
	def toPrint(self):
		print "id " + str(id(self.root)) + " value " + str(self.root.data)
		current = self.root.next
		count = 0
		while current.data != self.root.data and count < 10:
			print "id " + str(id(current)) + " value " + str(current.data)
			current = current.next
			count += 1

class Cache:
	def __init__(self, maxSize=1000):
		self.index = {}
		self.lru = DoublyLinkedList()
		self.maxSize = maxSize
		self.size = 0
	
	def set(self, key, value):
		if self.size >= self.maxSize:
			# If the cache is full, the least recently used element is deleted
			(key_del, _) = self.lru.removeLast()
			del self.index[key_del]
		else:
			self.size += 1
				
		# Add (value, key) pair to the cache
		node = Node((key, value))
		self.lru.insertHead(node)
		self.index[key] = node		
	
	def get(self, key):
		if key in self.index:
			# If key in cache, return the associated value
			node = self.index[key]
			self.lru.moveToHead(node)
			return node.data[1]
		else:
			# Returns None if the key is not present	
			return None



