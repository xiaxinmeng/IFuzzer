import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_lgettext_2():
    with open(LGettextTestCase.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    lgettext = t.lgettext
    with LGettextTestCase.assertDeprecated('lgettext'):
        LGettextTestCase.assertEqual(lgettext('mullusk'), b'bacon')
    with LGettextTestCase.assertDeprecated('lgettext'):
        LGettextTestCase.assertEqual(lgettext('spam'), b'spam')

LGettextTestCase = test_gettext.LGettextTestCase()
LGettextTestCase.setUp()
test_lgettext_2()
