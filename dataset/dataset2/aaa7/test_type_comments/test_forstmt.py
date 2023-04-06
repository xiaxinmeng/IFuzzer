import ast
import sys
import unittest
from test import support
import test_type_comments

def test_forstmt():
    for tree in TypeCommentTests.parse_all(test_type_comments.forstmt):
        TypeCommentTests.assertEqual(tree.body[0].type_comment, 'int')
    tree = TypeCommentTests.classic_parse(test_type_comments.forstmt)
    TypeCommentTests.assertEqual(tree.body[0].type_comment, None)

TypeCommentTests = test_type_comments.TypeCommentTests()
test_forstmt()
