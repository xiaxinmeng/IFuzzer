class TestLRUPy(TestLRU, unittest.TestCase):
    module = py_functools

class TestLRUC(TestLRU, unittest.TestCase):
    module = c_functools