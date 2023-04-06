from test.support import verbose, run_doctest
from test.support.os_helper import EnvironmentVarGuard
import unittest
import getopt
import types
import test_getopt

def test_libref_examples():
    s = "\n        Examples from the Library Reference:  Doc/lib/libgetopt.tex\n\n        An example using only Unix style options:\n\n\n        >>> import getopt\n        >>> args = '-a -b -cfoo -d bar a1 a2'.split()\n        >>> args\n        ['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']\n        >>> optlist, args = getopt.getopt(args, 'abc:d:')\n        >>> optlist\n        [('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]\n        >>> args\n        ['a1', 'a2']\n\n        Using long option names is equally easy:\n\n\n        >>> s = '--condition=foo --testing --output-file abc.def -x a1 a2'\n        >>> args = s.split()\n        >>> args\n        ['--condition=foo', '--testing', '--output-file', 'abc.def', '-x', 'a1', 'a2']\n        >>> optlist, args = getopt.getopt(args, 'x', [\n        ...     'condition=', 'output-file=', 'testing'])\n        >>> optlist\n        [('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x', '')]\n        >>> args\n        ['a1', 'a2']\n        "
    import types
    m = types.ModuleType('libreftest', s)
    run_doctest(m, verbose)

GetoptTests = test_getopt.GetoptTests()
test_libref_examples()
