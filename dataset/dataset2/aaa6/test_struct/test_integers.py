from collections import abc
import array
import math
import operator
import unittest
import struct
import sys
from test import support
from test.support.script_helper import assert_python_ok
import binascii
from random import randrange
import test_struct

def test_integers():
    import binascii

    class IntTester(unittest.TestCase):

        def __init__(StructTest, format):
            super(IntTester, StructTest).__init__(methodName='test_one')
            StructTest.format = format
            StructTest.code = format[-1]
            StructTest.byteorder = format[:-1]
            if not StructTest.byteorder in test_struct.byteorders:
                raise ValueError('unrecognized packing byteorder: %s' % StructTest.byteorder)
            StructTest.bytesize = struct.calcsize(format)
            StructTest.bitsize = StructTest.bytesize * 8
            if StructTest.code in tuple('bhilqn'):
                StructTest.signed = True
                StructTest.min_value = -2 ** (StructTest.bitsize - 1)
                StructTest.max_value = 2 ** (StructTest.bitsize - 1) - 1
            elif StructTest.code in tuple('BHILQN'):
                StructTest.signed = False
                StructTest.min_value = 0
                StructTest.max_value = 2 ** StructTest.bitsize - 1
            else:
                raise ValueError('unrecognized format code: %s' % StructTest.code)

        def test_one(StructTest, x, pack=struct.pack, unpack=struct.unpack, unhexlify=binascii.unhexlify):
            format = StructTest.format
            if StructTest.min_value <= x <= StructTest.max_value:
                expected = x
                if StructTest.signed and x < 0:
                    expected += 1 << StructTest.bitsize
                StructTest.assertGreaterEqual(expected, 0)
                expected = '%x' % expected
                if len(expected) & 1:
                    expected = '0' + expected
                expected = expected.encode('ascii')
                expected = unhexlify(expected)
                expected = b'\x00' * (StructTest.bytesize - len(expected)) + expected
                if StructTest.byteorder == '<' or (StructTest.byteorder in ('', '@', '=') and (not test_struct.ISBIGENDIAN)):
                    expected = test_struct.string_reverse(expected)
                StructTest.assertEqual(len(expected), StructTest.bytesize)
                got = pack(format, x)
                StructTest.assertEqual(got, expected)
                retrieved = unpack(format, got)[0]
                StructTest.assertEqual(x, retrieved)
                StructTest.assertRaises((struct.error, TypeError), unpack, format, b'\x01' + got)
            else:
                StructTest.assertRaises((OverflowError, ValueError, struct.error), pack, format, x)

        def run(StructTest):
            from random import randrange
            values = []
            for exp in range(StructTest.bitsize + 3):
                values.append(1 << exp)
            for i in range(StructTest.bitsize):
                val = 0
                for j in range(StructTest.bytesize):
                    val = val << 8 | randrange(256)
                values.append(val)
            values.extend([300, 700000, sys.maxsize * 4])
            for base in values:
                for val in (-base, base):
                    for incr in (-1, 0, 1):
                        x = val + incr
                        StructTest.test_one(x)

            class NotAnInt:

                def __int__(StructTest):
                    return 42

            class Indexable(object):

                def __init__(StructTest, value):
                    StructTest._value = value

                def __index__(StructTest):
                    return StructTest._value

            class BadIndex(object):

                def __index__(StructTest):
                    raise TypeError

                def __int__(StructTest):
                    return 42
            StructTest.assertRaises((TypeError, struct.error), struct.pack, StructTest.format, 'a string')
            StructTest.assertRaises((TypeError, struct.error), struct.pack, StructTest.format, randrange)
            StructTest.assertRaises((TypeError, struct.error), struct.pack, StructTest.format, 3 + 42j)
            StructTest.assertRaises((TypeError, struct.error), struct.pack, StructTest.format, NotAnInt())
            StructTest.assertRaises((TypeError, struct.error), struct.pack, StructTest.format, BadIndex())
            for obj in (Indexable(0), Indexable(10), Indexable(17), Indexable(42), Indexable(100), Indexable(127)):
                try:
                    struct.pack(format, obj)
                except:
                    StructTest.fail("integer code pack failed on object with '__index__' method")
            for obj in (Indexable(b'a'), Indexable('b'), Indexable(None), Indexable({'a': 1}), Indexable([1, 2, 3])):
                StructTest.assertRaises((TypeError, struct.error), struct.pack, StructTest.format, obj)
    for (code, byteorder) in test_struct.iter_integer_formats():
        format = byteorder + code
        t = IntTester(format)
        t.run()

StructTest = test_struct.StructTest()
test_integers()
