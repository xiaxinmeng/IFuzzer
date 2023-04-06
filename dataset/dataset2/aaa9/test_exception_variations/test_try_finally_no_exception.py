import unittest
import test_exception_variations

def test_try_finally_no_exception():
    hit_finally = False
    try:
        pass
    finally:
        hit_finally = True
    ExceptionTestCase.assertTrue(hit_finally)

ExceptionTestCase = test_exception_variations.ExceptionTestCase()
test_try_finally_no_exception()
