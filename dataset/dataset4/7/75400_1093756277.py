import unittest, test.support
from test.support.script_helper import assert_python_ok
import threading

def f123():
    pass

class SysModuleTest(unittest.TestCase):
    def test_current_frames(self):
        t = threading.Thread(target=f123)
        t.start()
        t.join()