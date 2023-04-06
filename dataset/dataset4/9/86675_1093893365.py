import logging

def rec():
	try:
		logging.error("foo")
	except:
		pass
	rec()
rec()