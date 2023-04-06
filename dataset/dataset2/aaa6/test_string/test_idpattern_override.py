import unittest
import string
from string import Template
import test_string

def test_idpattern_override():

    class PathPattern(Template):
        idpattern = '[_a-z][._a-z0-9]*'
    m = test_string.Mapping()
    m.bag = test_string.Bag()
    m.bag.foo = test_string.Bag()
    m.bag.foo.who = 'tim'
    m.bag.what = 'ham'
    s = PathPattern('$bag.foo.who likes to eat a bag of $bag.what')
    TestTemplate.assertEqual(s.substitute(m), 'tim likes to eat a bag of ham')

TestTemplate = test_string.TestTemplate()
test_idpattern_override()
