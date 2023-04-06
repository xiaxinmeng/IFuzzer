
import pyperf
runner = pyperf.Runner()

# tuple_new(): PyTuple_New(0): get empty tuple singleton
runner.timeit('tuple()', 'local_tuple()', setup='local_tuple=tuple', duplicate=1024)

# _PyTuple_FromArray([]): get empty tuple singleton
runner.timeit('tuple([])', 'local_tuple(empty_list)', setup='local_tuple=tuple; empty_list=[]', duplicate=1024)

# _PyTuple_FromArray([None]) -> _PyTuple_FromArray([None], 1)
runner.timeit('tuple([None])', 'local_tuple(items)', setup='local_tuple=tuple; items=[None]', duplicate=1024)

# _PyTuple_FromArray([1, 2, 3]) -> _PyTuple_FromArray([1, 2, 3], 3)
runner.timeit('tuple([1, 2, 3])', 'local_tuple(items)', setup='local_tuple=tuple; items=[1, 2, 3]', duplicate=1024)
