import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_fstrings():
    UnparseTestCase.check_src_roundtrip('f\'\'\'-{f"""*{f"+{f\'.{x}.\'}+"}*"""}-\'\'\'')
    UnparseTestCase.check_src_roundtrip('f"\\u2028{\'x\'}"')
    UnparseTestCase.check_src_roundtrip("f'{x}\\n'")
    UnparseTestCase.check_src_roundtrip('f\'\'\'{"""\n"""}\\n\'\'\'')
    UnparseTestCase.check_src_roundtrip('f\'\'\'{f"""{x}\n"""}\\n\'\'\'')

UnparseTestCase = test_unparse.UnparseTestCase()
test_fstrings()
