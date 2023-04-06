import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_ignore_comments_in_headers_issue36239():
    """Checks that comments like:

            #-#-#-#-#  messages.po (EdX Studio)  #-#-#-#-#

        are ignored.
        """
    with open(test_gettext.MOFILE, 'wb') as fp:
        fp.write(base64.decodebytes(test_gettext.GNU_MO_DATA_ISSUE_17898))
    with open(test_gettext.MOFILE, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
        GNUTranslationParsingTest.assertEqual(t.info()['plural-forms'], 'nplurals=2; plural=(n != 1);')

GNUTranslationParsingTest = test_gettext.GNUTranslationParsingTest()
test_ignore_comments_in_headers_issue36239()
