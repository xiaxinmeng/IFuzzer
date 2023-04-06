import pyperf

runner = pyperf.Runner()
runner.timeit(name="bench throw",
              stmt="g.throw(TypeError)",
              setup = """
def gen():
    while True:
        try:
            yield
        except Exception:
            pass
g = gen()
g.send(None)
""")