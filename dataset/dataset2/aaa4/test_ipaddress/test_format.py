import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_format():
    v6 = ipaddress.IPv6Address('::1.2.3.42')
    v6_pairs = [('b', '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000100000001100101010'), ('n', '0000000000000000000000000102032a'), ('x', '0000000000000000000000000102032a'), ('X', '0000000000000000000000000102032A'), ('_b', '0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0001_0000_0010_0000_0011_0010_1010'), ('_n', '0000_0000_0000_0000_0000_0000_0102_032a'), ('_x', '0000_0000_0000_0000_0000_0000_0102_032a'), ('_X', '0000_0000_0000_0000_0000_0000_0102_032A'), ('#b', '0b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000100000001100101010'), ('#n', '0x0000000000000000000000000102032a'), ('#x', '0x0000000000000000000000000102032a'), ('#X', '0X0000000000000000000000000102032A'), ('#_b', '0b0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0001_0000_0010_0000_0011_0010_1010'), ('#_n', '0x0000_0000_0000_0000_0000_0000_0102_032a'), ('#_x', '0x0000_0000_0000_0000_0000_0000_0102_032a'), ('#_X', '0X0000_0000_0000_0000_0000_0000_0102_032A'), ('s', '::102:32a'), ('', '::102:32a')]
    for (fmt, txt) in v6_pairs:
        AddressTestCase_v4.assertEqual(txt, format(v6, fmt))

AddressTestCase_v4 = test_ipaddress.AddressTestCase_v4()
test_format()
