import time
from threading import Timer

def do_work():
    x = 2 + 2
    print("It is", time.asctime(), "and 2+2 is", x)

def go():
    Timer(10, do_work, ()).start()  # schedule it in one minute