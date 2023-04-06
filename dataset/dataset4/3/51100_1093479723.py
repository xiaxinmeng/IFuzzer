#!/usr/bin/python
import threading, urllib

class MyThread (threading.Thread):
	def run(self):
		c = urllib.urlopen("http://www.google.com")