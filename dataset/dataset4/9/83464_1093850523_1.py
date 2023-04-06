
import unittest


class SomethingLikeInheritedUnitest(unittest.TestProgram):
    # parent_parser is used here: https://github.com/python/cpython/blob/master/Lib/unittest/main.py#L162
    parent = super().createParentArgParserAndReturnIt()
    parser = argparse.ArgumentParser(parents=[parent])
    parser.add_argument('--myarg1', ...)
    parser.add_argument('--myarg2', ...)
    return parser
