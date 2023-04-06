
import timeit
import typing
import _typing

def _timeit(m):
    print(m.__name__, timeit.timeit("cast(int, 1)", globals={"cast": m.cast}))

_timeit(typing)
_timeit(_typing)
