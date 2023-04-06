from multiprocessing import Process
from time import sleep
from os import getpid
 
def log(daemon_mode):
    while True:
        print('worker %i %s' % (getpid(), daemon_mode))
        sleep(3)
  
print('parent pid %i' % getpid())
a = Process(target=log, args=(0,), daemon=False)
a.start()
   
b = Process(target=log, args=(1,), daemon=True)
b.start()
   
while True:
    sleep(60)