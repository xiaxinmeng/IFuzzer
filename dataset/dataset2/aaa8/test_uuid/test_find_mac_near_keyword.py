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

def test_find_mac_near_keyword():
    data = '\nfake      Link encap:UNSPEC  hwaddr 00-00\ncscotun0  Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00\neth0      Link encap:Ethernet  HWaddr 12:34:56:78:90:ab\n'
    with mock.patch.multiple(BaseTestInternals.uuid, _MAC_DELIM=b':', _MAC_OMITS_LEADING_ZEROES=False, _get_command_stdout=mock_get_command_stdout(data)):
        mac = BaseTestInternals.uuid._find_mac_near_keyword(command='ifconfig', args='', keywords=[b'hwaddr'], get_word_index=lambda x: x + 1)
    BaseTestInternals.assertEqual(mac, 20015998341291)

BaseTestInternals = test_uuid.BaseTestInternals()
test_find_mac_near_keyword()
