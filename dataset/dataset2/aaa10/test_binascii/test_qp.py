import unittest
import binascii
import array
import re
from test.support import warnings_helper
import test_binascii

def test_qp():
    type2test = BinASCIITest.type2test
    a2b_qp = binascii.a2b_qp
    b2a_qp = binascii.b2a_qp
    a2b_qp(data=b'', header=False)
    try:
        a2b_qp(b'', **{1: 1})
    except TypeError:
        pass
    else:
        BinASCIITest.fail("binascii.a2b_qp(**{1:1}) didn't raise TypeError")
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=')), b'')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'= ')), b'= ')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'==')), b'=')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=\nAB')), b'AB')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=\r\nAB')), b'AB')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=\rAB')), b'')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=\rAB\nCD')), b'CD')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=AB')), b'\xab')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=ab')), b'\xab')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=AX')), b'=AX')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=XA')), b'=XA')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=AB')[:-1]), b'=A')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'_')), b'_')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'_'), header=True), b' ')
    BinASCIITest.assertRaises(TypeError, b2a_qp, foo='bar')
    BinASCIITest.assertEqual(a2b_qp(type2test(b'=00\r\n=00')), b'\x00\r\n\x00')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'\xff\r\n\xff\n\xff')), b'=FF\r\n=FF\r\n=FF')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'0' * 75 + b'\xff\r\n\xff\r\n\xff')), b'0' * 75 + b'=\r\n=FF\r\n=FF\r\n=FF')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'\x7f')), b'=7F')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'=')), b'=3D')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'_')), b'_')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'_'), header=True), b'=5F')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x y'), header=True), b'x_y')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x '), header=True), b'x=20')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x y'), header=True, quotetabs=True), b'x=20y')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x\ty'), header=True), b'x\ty')
    BinASCIITest.assertEqual(b2a_qp(type2test(b' ')), b'=20')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'\t')), b'=09')
    BinASCIITest.assertEqual(b2a_qp(type2test(b' x')), b' x')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'\tx')), b'\tx')
    BinASCIITest.assertEqual(b2a_qp(type2test(b' x')[:-1]), b'=20')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'\tx')[:-1]), b'=09')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'\x00')), b'=00')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'\x00\n')), b'=00\n')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'\x00\n'), quotetabs=True), b'=00\n')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x y\tz')), b'x y\tz')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x y\tz'), quotetabs=True), b'x=20y=09z')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x y\tz'), istext=False), b'x y\tz')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \ny\t\n')), b'x=20\ny=09\n')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \ny\t\n'), quotetabs=True), b'x=20\ny=09\n')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \ny\t\n'), istext=False), b'x =0Ay\t=0A')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \ry\t\r')), b'x \ry\t\r')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \ry\t\r'), quotetabs=True), b'x=20\ry=09\r')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \ry\t\r'), istext=False), b'x =0Dy\t=0D')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \r\ny\t\r\n')), b'x=20\r\ny=09\r\n')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \r\ny\t\r\n'), quotetabs=True), b'x=20\r\ny=09\r\n')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \r\ny\t\r\n'), istext=False), b'x =0D=0Ay\t=0D=0A')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \r\n')[:-1]), b'x \r')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x\t\r\n')[:-1]), b'x\t\r')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \r\n')[:-1], quotetabs=True), b'x=20\r')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x\t\r\n')[:-1], quotetabs=True), b'x=09\r')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x \r\n')[:-1], istext=False), b'x =0D')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'x\t\r\n')[:-1], istext=False), b'x\t=0D')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'.')), b'=2E')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'.\n')), b'=2E\n')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'.\r')), b'=2E\r')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'.\x00')), b'=2E=00')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'a.\n')), b'a.\n')
    BinASCIITest.assertEqual(b2a_qp(type2test(b'.a')[:-1]), b'=2E')

BinASCIITest = test_binascii.BinASCIITest()
test_qp()
