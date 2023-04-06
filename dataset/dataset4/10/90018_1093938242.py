import threading
import ctypes
from test import test_code

def test_free_different_thread():
    f = test_code.CoExtra().get_func()

    class ThreadTest(threading.Thread):
        def __init__(CoExtra, f, test):
            f.test = f

    test_code.SetExtra(f.__code__, test_code.FREE_INDEX, ctypes.c_voidp(500))
    tt = ThreadTest(f, f)
    test_code.CoExtra().assertEqual(test_code.LAST_FREED, 500)

test_free_different_thread()