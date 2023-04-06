class MyTest(unittest.TestCase):
    def setUp(self):
        raise Exception
    @unittest.expectedFailure
    def testSomething(self):
        assert False, "test method failed"