from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_2G, memuse=2)
def test_join(BaseStrTest, size):
    _ = BaseStrTest.from_latin1
    s = _('A') * size
    x = s.join([_('aaaaa'), _('bbbbb')])
    BaseStrTest.assertEqual(x.count(_('a')), 5)
    BaseStrTest.assertEqual(x.count(_('b')), 5)
    BaseStrTest.assertTrue(x.startswith(_('aaaaaA')))
    BaseStrTest.assertTrue(x.endswith(_('Abbbbb')))

BaseStrTest = test_bigmem.BaseStrTest()
test_join()
