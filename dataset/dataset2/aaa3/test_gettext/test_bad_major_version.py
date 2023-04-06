import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_bad_major_version():
    with open(test_gettext.MOFILE_BAD_MAJOR_VERSION, 'rb') as fp:
        with GettextTestCase2.assertRaises(OSError) as cm:
            gettext.GNUTranslations(fp)
        exception = cm.exception
        GettextTestCase2.assertEqual(exception.errno, 0)
        GettextTestCase2.assertEqual(exception.strerror, 'Bad version number 5')
        GettextTestCase2.assertEqual(exception.filename, test_gettext.MOFILE_BAD_MAJOR_VERSION)

GettextTestCase2 = test_gettext.GettextTestCase2()
test_bad_major_version()
