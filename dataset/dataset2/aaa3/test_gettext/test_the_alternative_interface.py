import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_the_alternative_interface():
    eq = GettextTestCase1.assertEqual
    with open(GettextTestCase1.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    t.install()
    eq(_('nudge nudge'), 'wink wink')
    t.install()
    eq(_('mullusk'), 'bacon')
    import builtins
    t.install(names=['gettext', 'lgettext'])
    eq(_, t.gettext)
    eq(builtins.gettext, t.gettext)
    eq(lgettext, t.lgettext)
    del builtins.gettext
    del builtins.lgettext

GettextTestCase1 = test_gettext.GettextTestCase1()
GettextTestCase1.setUp()
test_the_alternative_interface()
