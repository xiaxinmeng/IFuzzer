import unittest
from json.decoder import JSONDecoder

class Memo_Test(unittest.TestCase):
    def test_for_empty_memo(self):
        json_str = '{"a": 1}'
        decoder = JSONDecoder()
        decoder.decode(json_str)
        self.assertEqual(decoder.memo, {})

suite = unittest.TestSuite()
suite.addTest(Memo_Test("test_for_empty_memo"))
runner = unittest.TextTestRunner()
runner.run(suite)