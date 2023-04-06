import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_lgettext_output_encoding():
    with open(LGettextTestCase.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    lgettext = t.lgettext
    with LGettextTestCase.assertDeprecated('set_output_charset'):
        t.set_output_charset('utf-16')
    with LGettextTestCase.assertDeprecated('lgettext'):
        LGettextTestCase.assertEqual(lgettext('mullusk'), 'bacon'.encode('utf-16'))
    with LGettextTestCase.assertDeprecated('lgettext'):
        LGettextTestCase.assertEqual(lgettext('spam'), 'spam'.encode('utf-16'))

LGettextTestCase = test_gettext.LGettextTestCase()
LGettextTestCase.setUp()
test_lgettext_output_encoding()
