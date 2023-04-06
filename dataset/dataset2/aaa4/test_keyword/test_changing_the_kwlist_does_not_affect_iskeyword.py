import keyword
import unittest
import test_keyword

def test_changing_the_kwlist_does_not_affect_iskeyword():
    oldlist = keyword.kwlist
    Test_iskeyword.addCleanup(setattr, keyword, 'kwlist', oldlist)
    keyword.kwlist = ['its', 'all', 'eggs', 'beans', 'and', 'a', 'slice']
    Test_iskeyword.assertFalse(keyword.iskeyword('eggs'))

Test_iskeyword = test_keyword.Test_iskeyword()
test_changing_the_kwlist_does_not_affect_iskeyword()
