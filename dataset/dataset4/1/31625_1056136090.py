from pyperf import Runner
runner = Runner()

for haystack, needle in [
    ("""b'x' * 100_000""", """b'y'"""),
    ("""b'x' * 100_000""", """b'yz'"""),
    ("""b'x' * 100_000""", """b'xy'"""),
    ("""b'x' * 100_000""", """b'yx'"""),
    ("""b'ab' * 100_000""", """b'abracadabra'"""),
    ("""b'a' * 10_000 + b'b' * 10_000 + b'a' * 10_000""",
     """b'a' * 10_001"""),
]:
    runner.timeit(
        f"{needle} in {haystack}",
        setup=f"""\
haystack = {haystack}
needle = {needle}
import mmap
m = mmap.mmap(-1, len(haystack))
m.write(haystack)
m.seek(0)
""",
        stmt=f"m.find(needle)"
    )