def __init__(self):
	self.cnt = 0
	self.s0 = '\0' * 20
	self.gauss_next = None

def seed(self, a=None):
	if a is None:
		# Initialize from current time
		import time
		a = time.time()
	b = sha.new(repr(a)).digest()		
	self.s0 = sha.new(self.s0 + b).digest()