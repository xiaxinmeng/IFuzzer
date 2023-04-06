import ast
import sys
import unittest
from test import support
import test_type_comments

def test_nonasciidef():
    for tree in TypeCommentTests.parse_all(test_type_comments.nonasciidef):
        TypeCommentTests.assertEqual(tree.body[0].type_comment, '() -> àçčéñt')

TypeCommentTests = test_type_comments.TypeCommentTests()
test_nonasciidef()
