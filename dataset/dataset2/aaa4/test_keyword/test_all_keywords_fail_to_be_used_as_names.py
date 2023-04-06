import keyword
import unittest
import test_keyword

def test_all_keywords_fail_to_be_used_as_names():
    for key in keyword.kwlist:
        with Test_iskeyword.assertRaises(SyntaxError):
            exec(f'{key} = 42')

Test_iskeyword = test_keyword.Test_iskeyword()
test_all_keywords_fail_to_be_used_as_names()
