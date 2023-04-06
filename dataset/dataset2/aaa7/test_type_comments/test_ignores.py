import ast
import sys
import unittest
from test import support
import test_type_comments

def test_ignores():
    for tree in TypeCommentTests.parse_all(test_type_comments.ignores):
        TypeCommentTests.assertEqual([(ti.lineno, ti.tag) for ti in tree.type_ignores], [(2, ''), (5, ''), (8, '[excuse]'), (9, '=excuse'), (10, ' [excuse]'), (11, ' whatever')])
    tree = TypeCommentTests.classic_parse(test_type_comments.ignores)
    TypeCommentTests.assertEqual(tree.type_ignores, [])

TypeCommentTests = test_type_comments.TypeCommentTests()
test_ignores()
