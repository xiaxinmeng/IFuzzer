import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_bad_minor_version():
    with open(test_gettext.MOFILE_BAD_MINOR_VERSION, 'rb') as fp:
        gettext.GNUTranslations(fp)

GettextTestCase2 = test_gettext.GettextTestCase2()
test_bad_minor_version()
