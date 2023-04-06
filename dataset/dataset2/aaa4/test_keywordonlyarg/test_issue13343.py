import unittest
import test_keywordonlyarg

def test_issue13343():
    lambda *, k1=unittest: None

KeywordOnlyArgTestCase = test_keywordonlyarg.KeywordOnlyArgTestCase()
test_issue13343()
