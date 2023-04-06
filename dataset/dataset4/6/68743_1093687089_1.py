#!/usr/bin/python
__author__ = 'bee13oy'
import re
import os
import threading
timeout = 2
source = "(.*(.)?)*bcd\\t\\n\\r\\f\\a\\e\\071\\x3b\\$\\\\\?caxyz"
def run(source):
    regexp = re.compile(r''+source+'')
    sgroup = regexp.search(source)       
def handle():
        try:
            t = threading.Thread(target=run,args=(source,))
            t.setDaemon(True)
            t.start()
            t.join(timeout)
            print("finished...\n")
        except:
            print("exception ...\n")		
handle()