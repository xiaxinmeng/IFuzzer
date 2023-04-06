import unittest
import sys
from io import StringIO
from test import support
import test_print

def test_print_flush():

    class filelike:

        def __init__(TestPrint):
            TestPrint.written = ''
            TestPrint.flushed = 0

        def write(TestPrint, str):
            TestPrint.written += str

        def flush(TestPrint):
            TestPrint.flushed += 1
    f = filelike()
    print(1, file=f, end='', flush=True)
    print(2, file=f, end='', flush=True)
    print(3, file=f, flush=False)
    TestPrint.assertEqual(f.written, '123\n')
    TestPrint.assertEqual(f.flushed, 2)

    class noflush:

        def write(TestPrint, str):
            pass

        def flush(TestPrint):
            raise RuntimeError
    TestPrint.assertRaises(RuntimeError, print, 1, file=noflush(), flush=True)

TestPrint = test_print.TestPrint()
test_print_flush()
