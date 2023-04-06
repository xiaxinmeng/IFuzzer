class Demo(unittest.TestCase):

    def setUp(self):
        raise Exception('hi')

    def test_normal(self):
        # this should NOT be covered by expectedFailure
        pass

    @unittest.expectedFailure
    def test_expected_fail(self):
        pass