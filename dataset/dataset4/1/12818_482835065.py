import threading
import time
from unittest.mock import WaitableMock, patch, call

def call_after_sometime(func, *args, delay=1):
    time.sleep(delay)
    func(*args)

def foo(*args):
    pass

def bar(*args):
    pass

with patch('__main__.foo', WaitableMock(event_class=threading.Event)):
    with patch('__main__.bar', WaitableMock(event_class=threading.Event)):
        threading.Thread(target=call_after_sometime, args=(foo, 1), kwargs={'delay': 1}).start()
        threading.Thread(target=call_after_sometime, args=(bar, 2), kwargs={'delay': 1}).start()
        print("bar called with 1 ", bar.wait_until_called_with(2, timeout=2))
        print(bar.mock_calls)
        bar.assert_called_once_with(2)
        print("foo called with 1 ", foo.wait_until_called_with(timeout=2))
        print(foo.mock_calls)