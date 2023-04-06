import ast
import sys
import unittest
from test import support
import test_type_comments

def test_matmul():
    for tree in TypeCommentTests.parse_all(test_type_comments.matmul, minver=5):
        pass

TypeCommentTests = test_type_comments.TypeCommentTests()
test_matmul()
