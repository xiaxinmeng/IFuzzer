import threading
import subprocess
import time

l = threading.Lock() 

def f():
    l.acquire()  
    time.sleep(1)
    l.release()
 
t = threading.Thread(target=f)
t.start()

def g(l):
    l.acquire()
    l.release() 
    print('ohai')
