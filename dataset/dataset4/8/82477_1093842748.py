
class TestFailure(unittest.TestCase):

    @unittest.expectedFailure
    def test_expected_failure(self):
        raise TypeError()   # for example, a typo.
