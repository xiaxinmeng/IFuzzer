from unittest import TestCase, mock
from unittest import mock
import errno
import os
import tabnanny
import tokenize
import tempfile
import textwrap
from test.support import captured_stderr, captured_stdout, script_helper, findfile
from test.support.os_helper import unlink
import test_tabnanny

def test_format_witnesses():
    """Asserting formatter result by giving various input samples."""
    tests = [('Test', 'at tab sizes T, e, s, t'), ('', 'at tab size '), ('t', 'at tab size t'), ('  t  ', 'at tab sizes  ,  , t,  ,  ')]
    for (words, expected) in tests:
        with TestFormatWitnesses.subTest(words=words, expected=expected):
            TestFormatWitnesses.assertEqual(tabnanny.format_witnesses(words), expected)

TestFormatWitnesses = test_tabnanny.TestFormatWitnesses()
test_format_witnesses()
