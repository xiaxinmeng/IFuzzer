
from Cocoa import NSObject, NSThread
import time

class Runner(NSObject):
   def doit_(self, arg):
       print("hello world")
       print(NSThread.currentThread().isMainThread())


runner = Runner.alloc().init()

thread = NSThread.alloc().initWithTarget_selector_object_(runner, b"doit:", None)
thread.start()
print(thread)
time.sleep(1)
while thread.isExecuting():
    time.sleep(1)
