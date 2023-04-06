import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_lgettext():
    lgettext = gettext.lgettext
    ldgettext = gettext.ldgettext
    with LGettextTestCase.assertDeprecated('lgettext'):
        LGettextTestCase.assertEqual(lgettext('mullusk'), b'bacon')
    with LGettextTestCase.assertDeprecated('lgettext'):
        LGettextTestCase.assertEqual(lgettext('spam'), b'spam')
    with LGettextTestCase.assertDeprecated('ldgettext'):
        LGettextTestCase.assertEqual(ldgettext('gettext', 'mullusk'), b'bacon')
    with LGettextTestCase.assertDeprecated('ldgettext'):
        LGettextTestCase.assertEqual(ldgettext('gettext', 'spam'), b'spam')

LGettextTestCase = test_gettext.LGettextTestCase()
test_lgettext()
