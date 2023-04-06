import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_some_translations_with_context():
    eq = GettextTestCase1.assertEqual
    eq(gettext.pgettext('my context', 'nudge nudge'), 'wink wink (in "my context")')
    eq(gettext.pgettext('my other context', 'nudge nudge'), 'wink wink (in "my other context")')

GettextTestCase1 = test_gettext.GettextTestCase1()
test_some_translations_with_context()
