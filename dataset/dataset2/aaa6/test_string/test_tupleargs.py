import unittest
import string
from string import Template
import test_string

def test_tupleargs():
    eq = TestTemplate.assertEqual
    s = Template('$who ate ${meal}')
    d = dict(who=('tim', 'fred'), meal=('ham', 'kung pao'))
    eq(s.substitute(d), "('tim', 'fred') ate ('ham', 'kung pao')")
    eq(s.safe_substitute(d), "('tim', 'fred') ate ('ham', 'kung pao')")

TestTemplate = test_string.TestTemplate()
test_tupleargs()
