from test.support import run_with_locale
import collections.abc
from collections import namedtuple
import inspect
import pickle
import locale
import sys
import types
import unittest.mock
import weakref
import typing
import test_types

def test_duck_functional_gen():

    class Generator:
        """Emulates the following generator (very clumsy):

              def gen(fut):
                  result = yield fut
                  return result * 2
            """

        def __init__(CoroutineTests, fut):
            CoroutineTests._i = 0
            CoroutineTests._fut = fut

        def __iter__(CoroutineTests):
            return CoroutineTests

        def __next__(CoroutineTests):
            return CoroutineTests.send(None)

        def send(CoroutineTests, v):
            try:
                if CoroutineTests._i == 0:
                    assert v is None
                    return CoroutineTests._fut
                if CoroutineTests._i == 1:
                    raise StopIteration(v * 2)
                if CoroutineTests._i > 1:
                    raise StopIteration
            finally:
                CoroutineTests._i += 1

        def throw(CoroutineTests, tp, *exc):
            CoroutineTests._i = 100
            if tp is not GeneratorExit:
                raise tp

        def close(CoroutineTests):
            CoroutineTests.throw(GeneratorExit)

    @types.coroutine
    def foo():
        return Generator('spam')
    wrapper = foo()
    CoroutineTests.assertIsInstance(wrapper, types._GeneratorWrapper)

    async def corofunc():
        return await foo() + 100
    coro = corofunc()
    CoroutineTests.assertEqual(coro.send(None), 'spam')
    try:
        coro.send(20)
    except StopIteration as ex:
        CoroutineTests.assertEqual(ex.args[0], 140)
    else:
        CoroutineTests.fail('StopIteration was expected')

CoroutineTests = test_types.CoroutineTests()
test_duck_functional_gen()
