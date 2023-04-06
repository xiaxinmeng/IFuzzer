import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_timeit_globals_args():
    global _global_timer
    _global_timer = test_timeit.FakeTimer()
    t = timeit.Timer(stmt='_global_timer.inc()', timer=_global_timer)
    TestTimeit.assertRaises(NameError, t.timeit, number=3)
    timeit.timeit(stmt='_global_timer.inc()', timer=_global_timer, globals=globals(), number=3)
    local_timer = test_timeit.FakeTimer()
    timeit.timeit(stmt='local_timer.inc()', timer=local_timer, globals=locals(), number=3)

TestTimeit = test_timeit.TestTimeit()
test_timeit_globals_args()
