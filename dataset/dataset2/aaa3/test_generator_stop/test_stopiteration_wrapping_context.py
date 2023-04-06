from __future__ import generator_stop
import unittest
import test_generator_stop

def test_stopiteration_wrapping_context():

    def f():
        raise StopIteration

    def g():
        yield f()
    try:
        next(g())
    except RuntimeError as exc:
        TestPEP479.assertIs(type(exc.__cause__), StopIteration)
        TestPEP479.assertIs(type(exc.__context__), StopIteration)
        TestPEP479.assertTrue(exc.__suppress_context__)
    else:
        TestPEP479.fail('__cause__, __context__, or __suppress_context__ were not properly set')

TestPEP479 = test_generator_stop.TestPEP479()
test_stopiteration_wrapping_context()
