import multiprocessing
import threading
import time
from unittest.mock import WaitableMock, patch, call

def call_after_sometime(func, *args, delay=1):
    time.sleep(delay)
    func(*args)

def wraps(*args):
    return 1

def foo(*args):
    pass

def bar(*args):
    pass

with patch('__main__.foo', WaitableMock(event_class=threading.Event, wraps=wraps)):
    with patch('__main__.bar', WaitableMock(event_class=threading.Event)):
        # Test normal call
        threading.Thread(target=call_after_sometime, args=(foo, 1), kwargs={'delay': 1}).start()
        threading.Thread(target=call_after_sometime, args=(bar, 1), kwargs={'delay': 5}).start()
        print("foo called ", foo.wait_until_called(timeout=2))
        print("bar called ", bar.wait_until_called(timeout=2))
        foo.assert_called_once()
        bar.assert_not_called()