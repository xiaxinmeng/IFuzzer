import unittest
import string
from string import Template
import test_string

def test_percents():
    eq = TestTemplate.assertEqual
    s = Template('%(foo)s $foo ${foo}')
    d = dict(foo='baz')
    eq(s.substitute(d), '%(foo)s baz baz')
    eq(s.safe_substitute(d), '%(foo)s baz baz')

TestTemplate = test_string.TestTemplate()
test_percents()
