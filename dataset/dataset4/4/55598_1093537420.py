import doctest
import unittest
if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(doctest.DocFileSuite('README.txt',
    optionflags=doctest.ELLIPSIS))