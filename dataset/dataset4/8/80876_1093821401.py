
import doctest

class Tester:
    r"""Provide docstring for testing.

    >>> import warnings
    >>> from contextlib import redirect_stderr
    >>> from io import StringIO
    >>> sio = StringIO()
    >>> with redirect_stderr(sio):
    ...     warnings.warn("Warning 'containing' single quotes")
    >>> sio.getvalue()
    "...UserWarning: Warning 'containing' single quotes\n..."

    """


doctest.run_docstring_examples(
    Tester(),
    {},
    optionflags=doctest.ELLIPSIS,
)
