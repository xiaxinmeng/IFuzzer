import unittest

def simpleFunction59():
    a = 1
    try:
        return a
    finally:
        return a

class Tests(unittest.TestCase):
    def test_bug(self):
        for _ in range(10):
            simpleFunction59()