class TestFoo(unittest.TestCase):

    def test_foo(self):
        ret = doctest.run_docstring_examples(somefun, globals())
        self.assertFalse(ret[0].failed)