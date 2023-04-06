from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_13_genexp():
    TraceTestCase.run_test(test_sys_settrace.generator_example)
    tracer = TraceTestCase.make_tracer()
    sys.settrace(tracer.traceWithGenexp)
    test_sys_settrace.generator_example()
    sys.settrace(None)
    TraceTestCase.compare_events(test_sys_settrace.generator_example.__code__.co_firstlineno, tracer.events, test_sys_settrace.generator_example.events)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_13_genexp()
