def f():
    return "f result"

mocked_f = Mock(wraps=f)
coro_func = asyncio.coroutine(mocked_f)
print(loop.run_until_complete(coro_func()))
mocked_f.assert_called_once_with() 