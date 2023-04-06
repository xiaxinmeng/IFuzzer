import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_plural_form_error_issue17898():
    with open(test_gettext.MOFILE, 'wb') as fp:
        fp.write(base64.decodebytes(test_gettext.GNU_MO_DATA_ISSUE_17898))
    with open(test_gettext.MOFILE, 'rb') as fp:
        t = gettext.GNUTranslations(fp)

GNUTranslationParsingTest = test_gettext.GNUTranslationParsingTest()
test_plural_form_error_issue17898()
