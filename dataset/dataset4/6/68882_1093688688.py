from __future__ import print_function

from pyccp.unittest import SafeTestCase


class MyTest(SafeTestCase):

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test(self):
        print("creating")
        self.addCleanup(lambda: print("destroying"))