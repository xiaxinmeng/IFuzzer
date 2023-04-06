import unittest
from test import support
from test.support import import_helper
import builtins
import contextlib
import copy
import io
import os
import pickle
import sys
import weakref
from unittest import mock
import test_uuid

def test_find_under_heading():
    data = 'Name  Mtu   Network     Address           Ipkts Ierrs    Opkts Oerrs  Coll\nen0   1500  link#2      fe.ad.c.1.23.4   1714807956     0 711348489     0     0\n                        01:00:5e:00:00:01\nen0   1500  192.168.129 x071             1714807956     0 711348489     0     0\n                        224.0.0.1\nen0   1500  192.168.90  x071             1714807956     0 711348489     0     0\n                        224.0.0.1\n'
    with mock.patch.multiple(BaseTestInternals.uuid, _MAC_DELIM=b'.', _MAC_OMITS_LEADING_ZEROES=True, _get_command_stdout=mock_get_command_stdout(data)):
        mac = BaseTestInternals.uuid._find_mac_under_heading(command='netstat', args='-ian', heading=b'Address')
    BaseTestInternals.assertEqual(mac, 280019184198404)

BaseTestInternals = test_uuid.BaseTestInternals()
test_find_under_heading()
