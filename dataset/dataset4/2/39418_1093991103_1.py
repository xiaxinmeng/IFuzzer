class TwoWayDictionaryTestCase(unittest.TestCase):
    def testInit(self):
        d = TwoWayDictionary(foo='bar')
        self.failUnless('foo' in d)
        self.failUnless('bar' in d)