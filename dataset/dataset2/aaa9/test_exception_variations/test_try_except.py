import unittest
import test_exception_variations

def test_try_except():
    hit_except = False
    try:
        raise Exception('ahoy!')
    except:
        hit_except = True
    ExceptionTestCase.assertTrue(hit_except)

ExceptionTestCase = test_exception_variations.ExceptionTestCase()
test_try_except()
