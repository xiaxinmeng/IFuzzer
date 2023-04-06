import unittest
import ntpath
import os

class TestCase(unittest.TestCase):
    def test_getfullpathname(self):
        for count in xrange(1, 1000):
            name = u"x" * count
            path = ntpath._getfullpathname(name)
            self.assertEqual(os.path.basename(path), name)

if __name__ == '__main__':
    unittest.main()