import ast
import sys
import unittest
from test import support
import test_type_comments

def test_asyncvar():
    for tree in TypeCommentTests.parse_all(test_type_comments.asyncvar, maxver=6):
        pass

TypeCommentTests = test_type_comments.TypeCommentTests()
test_asyncvar()
