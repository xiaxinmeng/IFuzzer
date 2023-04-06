#!/usr/bin/python
__author__ = 'bee13oy'
import re
import threading
timeout = 2
source = "(.*(.)?)*bcd\\t\\n\\r\\f\\a\\e\\071\\x3b\\$\\\\\?caxyz"
def run(source):
    while(1):
        print("test1")   
def handle():
        try:
            t = threading.Thread(target=run,args=(source,))
            t.setDaemon(True)
            t.start()
            t.join(timeout)
            print("thread finished...It's an normal case!\n")
        except:
            print("exception ...\n")		
handle()