
import unittest


def d():
  assert 2 == 3

def c():
  d()

def b():
  c()

def a():
  try:
    b()
  except Exception as e:
    assert 1 == 2


class MyTest(unittest.TestCase):

  def testException(self):
    a()


if __name__ == '__main__':
  unittest.main()
