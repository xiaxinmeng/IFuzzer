def bar():
   yield 5

foo = types.coroutine(bar)