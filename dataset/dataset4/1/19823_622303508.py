import re
import sys


def f():
    exc, exc_value, tb = sys.exc_info()
    print(f'CLEARING FRAME: {tb.tb_frame!r}')
    tb.tb_frame.clear()

def g():
    # Uncommenting the following line caused the tb_frame.clear() line
    # above to exhibit the following platform-specific behavior:
    # 1) On Mac, this is logged to stderr
    #  > TypeError: print_exception(): Exception expected for value,
    #    NoneType found
    # 2) On Fedora 32, the following error happens:
    #  > Fatal Python error: Segmentation fault
    data = re.compile('xxx')

    try:
        yield
    except Exception:
        f()

gen = g()
gen.send(None)
gen.throw(ValueError)