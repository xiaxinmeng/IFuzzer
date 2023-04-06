import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_fstrings_complicated():
    UnparseTestCase.check_ast_roundtrip('f\'\'\'{"\'"}\'\'\'')
    UnparseTestCase.check_ast_roundtrip('f\'\'\'-{f"""*{f"+{f\'.{x}.\'}+"}*"""}-\'\'\'')
    UnparseTestCase.check_ast_roundtrip('f\'\'\'-{f"""*{f"+{f\'.{x}.\'}+"}*"""}-\'single quote\\\'\'\'\'')
    UnparseTestCase.check_ast_roundtrip('f"""{\'\'\'\n\'\'\'}"""')
    UnparseTestCase.check_ast_roundtrip('f"""{g(\'\'\'\n\'\'\')}"""')
    UnparseTestCase.check_ast_roundtrip('f"a\\r\\nb"')
    UnparseTestCase.check_ast_roundtrip('f"\\u2028{\'x\'}"')

UnparseTestCase = test_unparse.UnparseTestCase()
test_fstrings_complicated()
