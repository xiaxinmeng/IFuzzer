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

def test_find_under_heading_ipv6():
    data = 'Name    Mtu Network       Address              Ipkts Ierrs Idrop    Opkts Oerrs  Coll\nvtnet  1500 <Link#1>      52:54:00:9d:0e:67    10017     0     0     8174     0     0\nvtnet     - fe80::%vtnet0 fe80::5054:ff:fe9        0     -     -        4     -     -\nvtnet     - 192.168.122.0 192.168.122.45        8844     -     -     8171     -     -\nlo0   16384 <Link#2>      lo0                 260148     0     0   260148     0     0\nlo0       - ::1/128       ::1                    193     -     -      193     -     -\n                          ff01::1%lo0\n                          ff02::2:2eb7:74fa\n                          ff02::2:ff2e:b774\n                          ff02::1%lo0\n                          ff02::1:ff00:1%lo\nlo0       - fe80::%lo0/64 fe80::1%lo0              0     -     -        0     -     -\n                          ff01::1%lo0\n                          ff02::2:2eb7:74fa\n                          ff02::2:ff2e:b774\n                          ff02::1%lo0\n                          ff02::1:ff00:1%lo\nlo0       - 127.0.0.0/8   127.0.0.1           259955     -     -   259955     -     -\n                          224.0.0.1\n'
    with mock.patch.multiple(BaseTestInternals.uuid, _MAC_DELIM=b':', _MAC_OMITS_LEADING_ZEROES=False, _get_command_stdout=mock_get_command_stdout(data)):
        mac = BaseTestInternals.uuid._find_mac_under_heading(command='netstat', args='-ian', heading=b'Address')
    BaseTestInternals.assertEqual(mac, 90520741023335)

BaseTestInternals = test_uuid.BaseTestInternals()
test_find_under_heading_ipv6()
