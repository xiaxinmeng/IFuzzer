class MinidomTest(unittest.TestCase):
    def confirm(self, test, testname = "Test"):
        self.assertTrue(test, testname)