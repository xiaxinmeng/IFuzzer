from unittest import TestCase, skipIf

#@skipIf(True, "Skip Testing")
class Tests(TestCase):
  def test_skip(self):
    "this test will fail - if not skipped"
    print('asserting')
    self.assertEqual(0, 1)