def foo():
    try:
        1/0
    except Exception as err:
        foo = 1

import dis
dis.dis(foo)