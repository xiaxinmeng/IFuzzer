import unittest
import test_exception_variations

def test_try_except_finally():
    hit_except = False
    hit_finally = False
    try:
        raise Exception('yarr!')
    except:
        hit_except = True
    finally:
        hit_finally = True
    ExceptionTestCase.assertTrue(hit_except)
    ExceptionTestCase.assertTrue(hit_finally)

ExceptionTestCase = test_exception_variations.ExceptionTestCase()
test_try_except_finally()
