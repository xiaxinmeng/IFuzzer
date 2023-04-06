import logging

def rec():
	logging.error("foo")
	rec()
rec()