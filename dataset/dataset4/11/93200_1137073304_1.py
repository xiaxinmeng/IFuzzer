import pyperf
import _testcapi
runner = pyperf.Runner()
runner.bench_time_func('bench', _testcapi.bench_encode)