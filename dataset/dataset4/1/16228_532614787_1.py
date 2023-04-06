import unittest


class Ham:
    def spam(self):
        pass

    eggs = spam

    def bacon(self):
        pass


class TestHam(unittest.TestCase):
    def test_eggs_is_eggs(self):
        h = Ham()
        self.assertIs(h.eggs, h.eggs)

    def test_spam_is_spam(self):
        h = Ham()
        self.assertIs(h.spam, h.spam)

    def test_spam_is_eggs(self):
        h = Ham()
        self.assertIs(h.spam, h.eggs)

    def test_eggs_equal_eggs(self):
        h = Ham()
        self.assertEqual(h.eggs, h.eggs)

    def test_spam_equal_spam(self):
        h = Ham()
        self.assertEqual(h.spam, h.spam)

    def test_spam_equal_eggs(self):
        h = Ham()
        self.assertEqual(h.spam, h.eggs)

    def test_spam_equal_bacon(self):
        h = Ham()
        self.assertEqual(h.spam, h.bacon)


if __name__ == "__main__":
    unittest.main()