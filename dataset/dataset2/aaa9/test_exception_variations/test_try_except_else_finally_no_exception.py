import unittest
import test_exception_variations

def test_try_except_else_finally_no_exception():
    hit_except = False
    hit_else = False
    hit_finally = False
    try:
        pass
    except:
        hit_except = True
    else:
        hit_else = True
    finally:
        hit_finally = True
    ExceptionTestCase.assertFalse(hit_except)
    ExceptionTestCase.assertTrue(hit_finally)
    ExceptionTestCase.assertTrue(hit_else)

ExceptionTestCase = test_exception_variations.ExceptionTestCase()
test_try_except_else_finally_no_exception()
