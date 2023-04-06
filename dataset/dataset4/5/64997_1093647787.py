import testtools

class TestConfigTrueValue(testtools.TestCase):
    def test_testEquals(self):
        reference = "reference-0123456789012345678901234567890123456789"
        def function_under_test():
            return "actual-0123456789012345678901234567890123456789"
        self.assertEquals(function_under_test(), reference)