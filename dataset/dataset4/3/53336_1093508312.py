import unittest
import urllib2

class DownloadUrlTest(unittest.TestCase):
    def testDownloadUrl(self):
        opener = urllib2.build_opener()
        handle = opener.open('http://localhost/', timeout=60)
        handle.info()
        data = handle.read()
        self.assertNotEqual(data, '')

if __name__ == "__main__":
    unittest.main()