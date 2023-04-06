from __future__ import generator_stop
import unittest
import test_generator_stop

def test_stopiteration_wrapping():

    def f():
        raise StopIteration

    def g():
        yield f()
    with TestPEP479.assertRaisesRegex(RuntimeError, 'generator raised StopIteration'):
        next(g())

TestPEP479 = test_generator_stop.TestPEP479()
test_stopiteration_wrapping()
