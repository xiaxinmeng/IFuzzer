import keyword
import unittest
import test_keyword

def test_uppercase_true_is_not_a_keyword():
    Test_iskeyword.assertFalse(keyword.iskeyword('TRUE'))

Test_iskeyword = test_keyword.Test_iskeyword()
test_uppercase_true_is_not_a_keyword()
