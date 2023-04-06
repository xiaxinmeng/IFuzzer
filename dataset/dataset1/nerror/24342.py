async def foo():
    return 'spam'

def wrapper(coro):
    async def wrap(coro):
        print('before')
        try:
            return await coro
        finally:
            print('after')
    return wrap(coro)

import sys
# sys.set_coroutine_wrapper(wrapper)
print(foo().send(None))
