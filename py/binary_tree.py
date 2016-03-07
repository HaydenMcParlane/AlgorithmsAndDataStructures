#
#	Binary search tree implementation
#	There are two implementations to test:
#		1. Using node class and separate objects in memory.
#		2. Using array index manipulations instead of objects
#		dispersed throughout memory (this isn't exactly the case
#		in python because python implements lists as arrays of
#		pointers meaning the actual nodes aren't necessarily 
#		localized. This may eliminate the data localization
#		optimization experienced in other languages that store
#		copies of the nodes contiguously in memory).
#	@author: Hayden McParlane
#	@creation-date: 3.5.2016
class BinarySearchTree(object):
	def __init__(self, list_of_vals=None):
		if list_of_vals is not None:
			self.root = Node(list_of_vals[0]) # TODO: Better way to implement this?
			self.count = len(list_of_vals)
			for i in range(len(list_of_vals))[1:]:
				self.insert(self.root, list_of_vals[i])

	def insert(self, node, value):
		if value <= node.value:
			if node.left is None:
				# Insert new value
				new_node = Node(value)
				new_node.parent = node
				node.left = new_node
				return
			else:
				# Recursively call same function on left child
				self.insert(node.left, value)
		elif value > node.value:
			if node.right is None:
				# Insert new node
				new_node = Node(value)
				new_node.parent = node
				node.right = new_node
			else:
				# Recursively call same function on right child
				self.insert(node.right, value)
		else:
			raise ValueError("Something was wrong with entered value") 

	def delete(self, node, value):
		pass

	def search(self, node, value):
		found = False
		if value == node.value:
			found = True
		elif value < node.value:
			if node.left is not None:
				found = self.search(node.left, value)
		elif value > node.value:
			if node.right is not None:
				found = self.search(node.right, value)
		return found


	def print_vals(self, node):
		if node.left is None and node.right is None:
			print node.value
		else:
			if node.left is not None:
				self.print_vals(node.left)
			print node.value
			if node.right is not None:
				self.print_vals(node.right)

# The node needs to contain
class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.parent = None
		self.right = None
		self.left = None
