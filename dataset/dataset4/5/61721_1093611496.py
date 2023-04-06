class AbstractTestCase(unittest.TestCase, metaclass=abc.ABCMeta):
  ...

class FooTest(AbstractTestCase):
  def foo(self):
    return 1