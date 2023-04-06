pytb
"""
Traceback (most recent call last):
  File "tests/run/test_coroutines_pep492.pyx", line 245, in test_coroutines_pep492.CoroutineTest.test_func_5 (test_coroutines_pep492.c:13445)
    for el in bar():
  File "/opt/python3.5/lib/python3.5/types.py", line 197, in wrapped
    'non-coroutine: {!r}'.format(coro))
TypeError: callable wrapped with types.coroutine() returned non-coroutine: <generator object at 0x7f178c458898>
"""
