import pyperf

runner = pyperf.Runner()
runner.timeit(name="bench bytearray",
              stmt="bytearray([42]*10000)",)