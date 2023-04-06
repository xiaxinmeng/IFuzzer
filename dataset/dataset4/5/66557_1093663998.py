from time import sleep
from concurrent.futures import ThreadPoolExecutor

def func():
    print("start")
    sleep(10)
    print("stop")

ex = ThreadPoolExecutor(1)

# New workers will be scheduled when an event
# is triggered (i.e. pyinotify events)
ex.submit(func)

# Dummy sleep
sleep(60)