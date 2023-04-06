import sys
import thread

class Dummy:
	def worker(self):
		raise AttributeError