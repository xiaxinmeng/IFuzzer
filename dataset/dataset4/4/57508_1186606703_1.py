import pyperf

from textwrap import dedent


SETUP_DEF=dedent("""
    import sqlite3
    cx = sqlite3.connect(":memory:")
""")
SETUP_ROW=dedent("""
    import sqlite3
    cx = sqlite3.connect(":memory:")
    cx.row_factory = sqlite3.Row
""")
SETUP_NAMED=dedent("""
    import sqlite3
    cx = sqlite3.connect(":memory:")
    cx.row_factory = sqlite3.NamedTupleRow
""")
STMT=dedent("""
    cx.execute("select 1 as 'a', 2 as 'b'").fetchall()
""")

runner = pyperf.Runner()
runner.timeit(name="default", stmt=STMT, setup=SETUP_DEF)
runner.timeit(name="row", stmt=STMT, setup=SETUP_ROW)
runner.timeit(name="named", stmt=STMT, setup=SETUP_NAMED)