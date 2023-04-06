def baditer():
    raise TypeError
    yield 1

import sets
sets.Set(baditer())