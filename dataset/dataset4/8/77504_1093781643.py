
def good_exception():
    raise Exception('something bad happened')

def bad_exception():
    return next(iter([]))

def good(n):
    return good_exception() + n

def bad(n):
    return n - bad_exception()

import traceback

try:
    max(good(i) for i in range(4)) # desirable behaviour
except:
    traceback.print_exc()

try:
    min(bad(i) for i in range(7)) # unhelpful error message
except:
    traceback.print_exc()
