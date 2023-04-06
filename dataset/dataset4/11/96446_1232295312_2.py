
import pyperf
import _testcapi
runner = pyperf.Runner()
runner.bench_time_func('tuple_new', _testcapi.bench2)
