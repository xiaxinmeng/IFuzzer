
import doctest

class Tester:
    r"""Provide docstring for testing.

    >>> import warnings
    >>> from contextlib import redirect_stderr
    >>> from io import StringIO
    >>> sio = StringIO()
    >>> with redirect_stderr(sio):
    ...     warnings.warn("Warning with no quotes")
    >>> sio.getvalue()
    '...'

    """

doctest.run_docstring_examples(
    Tester(),
    {},
    optionflags=doctest.ELLIPSIS,
)
