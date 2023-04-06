class Test(TestCase):

    def test_good(self):
        self.assertTrue(1.0)

    def test_bad(self):
        self.assertFalse(1.0)

    @skip
    def test_bad_skip(self):
        self.assertFalse(1.0)