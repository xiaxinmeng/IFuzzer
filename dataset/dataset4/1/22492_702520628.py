import pyperf

runner = pyperf.Runner()
runner.timeit(name="bench range compute",
              stmt="""
v = a[100:200]
vs = a[s]
""",
setup= """
a = range(0, 11111111)
s = slice(100, 200)
""")