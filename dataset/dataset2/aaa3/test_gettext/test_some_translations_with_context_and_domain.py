import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_some_translations_with_context_and_domain():
    eq = GettextTestCase2.assertEqual
    eq(gettext.dpgettext('gettext', 'my context', 'nudge nudge'), 'wink wink (in "my context")')
    eq(gettext.dpgettext('gettext', 'my other context', 'nudge nudge'), 'wink wink (in "my other context")')

GettextTestCase2 = test_gettext.GettextTestCase2()
test_some_translations_with_context_and_domain()
