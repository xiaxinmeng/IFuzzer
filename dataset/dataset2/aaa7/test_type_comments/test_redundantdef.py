import ast
import sys
import unittest
from test import support
import test_type_comments

def test_redundantdef():
    for tree in TypeCommentTests.parse_all(test_type_comments.redundantdef, maxver=0, expected_regex='^Cannot have two type comments on def'):
        pass

TypeCommentTests = test_type_comments.TypeCommentTests()
test_redundantdef()
