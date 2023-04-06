import time
import threading
import Queue

thqueue = Queue.Queue()
thevent = threading.Event()

def t():
	thevent.set()
	item = thqueue.get()