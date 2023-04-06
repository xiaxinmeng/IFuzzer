import unittest
import test_exception_variations

def test_try_except_else():
    hit_except = False
    hit_else = False
    try:
        raise Exception('foo!')
    except:
        hit_except = True
    else:
        hit_else = True
    ExceptionTestCase.assertFalse(hit_else)
    ExceptionTestCase.assertTrue(hit_except)

ExceptionTestCase = test_exception_variations.ExceptionTestCase()
test_try_except_else()
