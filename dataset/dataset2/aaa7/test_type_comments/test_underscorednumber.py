import ast
import sys
import unittest
from test import support
import test_type_comments

def test_underscorednumber():
    for tree in TypeCommentTests.parse_all(test_type_comments.underscorednumber, minver=6):
        pass

TypeCommentTests = test_type_comments.TypeCommentTests()
test_underscorednumber()
