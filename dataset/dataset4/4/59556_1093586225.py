class MyTest(unittest.TestCase):

    def run(self, result=None):
        with my_context_manager() as foo:
            # Do stuff.
            super(MyTest, self).run(result)