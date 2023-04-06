import unittest
class Exmpl(unittest.TestCase):
  pass
Exmpl.testBug = lambda self: 1+2
if (__name__ == '__main__'):
  unittest.main()