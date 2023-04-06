import unittest
from json.decoder import JSONDecoder
from json.scanner import py_make_scanner

class Memo_Test(unittest.TestCase):
    def test_for_empty_memo(self):
        json_str = '{"a": 1}'
        decoder = JSONDecoder()
        decoder.scan_once = py_make_scanner(decoder)
        result = decoder.decode(json_str)
        self.assertEqual(result, {"a":1})
        self.assertEqual(decoder.memo, {})

suite = unittest.TestSuite()
suite.addTest(Memo_Test("test_for_empty_memo"))
runner = unittest.TextTestRunner()
runner.run(suite)