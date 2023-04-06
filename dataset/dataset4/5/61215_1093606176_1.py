import multiprocessing
import threading
import time
from unittest.mock import WaitableMock, patch

def call_after_sometime(func, delay=1):
    time.sleep(delay)
    func()

def foo():
    pass

def bar():
    pass

with patch('__main__.foo', WaitableMock(event_class=threading.Event)):
    with patch('__main__.bar', WaitableMock(event_class=threading.Event)):
        threading.Thread(target=call_after_sometime, args=(foo, 1)).start()
        threading.Thread(target=call_after_sometime, args=(bar, 5)).start()
        print("foo called ", foo.wait_until_called(timeout=2)) # successful
        print("bar called ", bar.wait_until_called(timeout=2)) # times out
        foo.assert_called_once()
        bar.assert_not_called()
        # Wait for the bar's thread to complete to verify call is registered
        time.sleep(5)
        bar.assert_called_once()