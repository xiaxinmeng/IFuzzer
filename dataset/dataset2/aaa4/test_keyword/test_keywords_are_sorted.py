import keyword
import unittest
import test_keyword

def test_keywords_are_sorted():
    Test_iskeyword.assertListEqual(sorted(keyword.kwlist), keyword.kwlist)

Test_iskeyword = test_keyword.Test_iskeyword()
test_keywords_are_sorted()
