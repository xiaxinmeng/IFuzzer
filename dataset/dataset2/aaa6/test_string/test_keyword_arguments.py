import unittest
import string
from string import Template
import test_string

def test_keyword_arguments():
    eq = TestTemplate.assertEqual
    s = Template('$who likes $what')
    eq(s.substitute(who='tim', what='ham'), 'tim likes ham')
    eq(s.substitute(dict(who='tim'), what='ham'), 'tim likes ham')
    eq(s.substitute(dict(who='fred', what='kung pao'), who='tim', what='ham'), 'tim likes ham')
    s = Template('the mapping is $mapping')
    eq(s.substitute(dict(foo='none'), mapping='bozo'), 'the mapping is bozo')
    eq(s.substitute(dict(mapping='one'), mapping='two'), 'the mapping is two')
    s = Template('the TestTemplate is $TestTemplate')
    eq(s.substitute(TestTemplate='bozo'), 'the TestTemplate is bozo')

TestTemplate = test_string.TestTemplate()
test_keyword_arguments()
