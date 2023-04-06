import keyword
import unittest
import test_keyword

def test_async_and_await_are_keywords():
    Test_iskeyword.assertIn('async', keyword.kwlist)
    Test_iskeyword.assertIn('await', keyword.kwlist)

Test_iskeyword = test_keyword.Test_iskeyword()
test_async_and_await_are_keywords()
