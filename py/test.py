#
#	Testing sandbox for python
#

class A(object):
	@staticmethod
	def staticf():
		print "This is static method"

	@classmethod
	def functionA(self):
		print "This is class method"

	def __repr__(self):
		return "Printable A or sub"

class B(A):
	def bizzle(self):
		print "bizzle"

def main():
	print "You in main!"

if __name__ == '__main__':
	main()
