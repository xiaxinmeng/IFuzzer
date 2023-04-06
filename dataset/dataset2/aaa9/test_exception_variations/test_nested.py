import unittest
import test_exception_variations

def test_nested():
    hit_finally = False
    hit_inner_except = False
    hit_inner_finally = False
    try:
        try:
            raise Exception('inner exception')
        except:
            hit_inner_except = True
        finally:
            hit_inner_finally = True
    finally:
        hit_finally = True
    ExceptionTestCase.assertTrue(hit_inner_except)
    ExceptionTestCase.assertTrue(hit_inner_finally)
    ExceptionTestCase.assertTrue(hit_finally)

ExceptionTestCase = test_exception_variations.ExceptionTestCase()
test_nested()
