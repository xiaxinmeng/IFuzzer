import multiprocessing

def f(m):
	print(m)

class P:
	def __init__(self, msg):
		self.msg = msg
	
	def start(self):
		p = multiprocessing.Process(target=f, args=(self.msg,))
		p.start()
# 