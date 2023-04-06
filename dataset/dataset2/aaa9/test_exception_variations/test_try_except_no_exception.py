import unittest
import test_exception_variations

def test_try_except_no_exception():
    hit_except = False
    try:
        pass
    except:
        hit_except = True
    ExceptionTestCase.assertFalse(hit_except)

ExceptionTestCase = test_exception_variations.ExceptionTestCase()
test_try_except_no_exception()
