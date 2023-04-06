import keyword
import unittest
import test_keyword

def test_true_is_a_keyword():
    Test_iskeyword.assertTrue(keyword.iskeyword('True'))

Test_iskeyword = test_keyword.Test_iskeyword()
test_true_is_a_keyword()
