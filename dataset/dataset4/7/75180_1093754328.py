def test_something(self):

    for info in CASES:
       with self.subTest(info):
          self.assert_something(info)