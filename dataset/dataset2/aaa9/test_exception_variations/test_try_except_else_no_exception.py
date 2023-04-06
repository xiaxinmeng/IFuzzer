import unittest
import test_exception_variations

def test_try_except_else_no_exception():
    hit_except = False
    hit_else = False
    try:
        pass
    except:
        hit_except = True
    else:
        hit_else = True
    ExceptionTestCase.assertFalse(hit_except)
    ExceptionTestCase.assertTrue(hit_else)

ExceptionTestCase = test_exception_variations.ExceptionTestCase()
test_try_except_else_no_exception()
