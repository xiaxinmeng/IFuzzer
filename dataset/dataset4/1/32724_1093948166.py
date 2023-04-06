class fred:
	def __init__(self):
		self.indirectFunc = self.theFunc

	def theFunc(self):
		return "blah"

def test():
	f = fred()
	del f


if __name__ == "__main__":
	for x in xrange(1000):
		test()
		