#
#	A heap implementation
#	@author: Hayden McParlane

import math

ceil = math.ceil
log = math.log

# Note: Every time want to traverse left => 2idx, right => 2idx + 1
class Heap(object):
	# TODO: Implement capability to choose min or max
	# heap
	def __init__(self, max=True):
		super(Heap, self).__init__()
		_heap = []
		_last = None

	def insert(self, number):
		# 1. Insert value at end of heap
		length = len(_heap)
		
		# 1.1 If no elements, insert as root node
		if length == 0:
			_heap[0] = number
		else:
			# 1.2 Insert in next available position

		# 2. Heapify
		
		pass
	
	def remove(self):
		pass

	def _heapify(self):
		pass
