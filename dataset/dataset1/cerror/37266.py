import _testcapi
import time

code = """
import threading
from time import sleep

def func():
    print("hello from daemon thread")
    sleep(0.2)
    print("code run after interpreter death...")
    sleep(0.1)
    print("does it crash?")
    sleep(0.1)
    print("still alive?")
    sleep(0.1)

thread = threading.Thread(target=func, daemon=True)
thread.start()
# what happens now?
sleep(0.1)
"""
_testcapi.run_in_subinterp(code)
# give time to the daemon thread to crash
time.sleep(1)
