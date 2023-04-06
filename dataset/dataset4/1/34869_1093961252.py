def whathdr(filename):
	"""Recognize sound headers"""
	f = open(filename, 'rb')
	h = f.read(512)
...