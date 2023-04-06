
from threading import threaded
import time

@threaded
def hello(who):
    time.sleep(10)
    print("Hello,", who)

hello("World")
