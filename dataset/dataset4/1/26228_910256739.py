from asyncio import iscoroutine, run
from types import coroutine


@coroutine
def coro():
    yield


def not_coro():
    yield


print(iscoroutine(coro()))     # True
print(iscoroutine(not_coro())) # True