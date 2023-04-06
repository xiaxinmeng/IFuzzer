import pyperf

runner = pyperf.Runner()
runner.timeit(name="bench long divide",
              stmt="""
for i in range(1, 256):
    a = 10000 // i
""")