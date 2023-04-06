import keyword
import unittest
import test_keyword

def test_none_value_is_not_a_keyword():
    Test_iskeyword.assertFalse(keyword.iskeyword(None))

Test_iskeyword = test_keyword.Test_iskeyword()
test_none_value_is_not_a_keyword()
