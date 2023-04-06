import greenlet
import sqlite3


class _ErrorContainer(object):
    error = None


def _expect_raises_fn(fn):
    ec = _ErrorContainer()
    try:
        fn()
    except Exception as err:
        assert str(err) == "this is a test"

        # assign the exception context outside of the except
        # is necessary
        ec.error = err