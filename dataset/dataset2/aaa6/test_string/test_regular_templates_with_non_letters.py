import unittest
import string
from string import Template
import test_string

def test_regular_templates_with_non_letters():
    s = Template('$_wh0_ likes ${_w_h_a_t_} for ${mea1}')
    d = dict(_wh0_='tim', _w_h_a_t_='ham', mea1='dinner')
    TestTemplate.assertEqual(s.substitute(d), 'tim likes ham for dinner')

TestTemplate = test_string.TestTemplate()
test_regular_templates_with_non_letters()
