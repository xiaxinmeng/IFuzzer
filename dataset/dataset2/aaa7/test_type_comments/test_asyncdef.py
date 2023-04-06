import ast
import sys
import unittest
from test import support
import test_type_comments

def test_asyncdef():
    for tree in TypeCommentTests.parse_all(test_type_comments.asyncdef, minver=5):
        TypeCommentTests.assertEqual(tree.body[0].type_comment, '() -> int')
        TypeCommentTests.assertEqual(tree.body[1].type_comment, '() -> int')
    tree = TypeCommentTests.classic_parse(test_type_comments.asyncdef)
    TypeCommentTests.assertEqual(tree.body[0].type_comment, None)
    TypeCommentTests.assertEqual(tree.body[1].type_comment, None)

TypeCommentTests = test_type_comments.TypeCommentTests()
test_asyncdef()
