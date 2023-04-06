class JSONEncodingTests:
    def test_encode1(self):
        self.assertEquals(self.encode("foo"), "bar")
    # etc.

class CJSONEncodingTests(JSONEncodingTests, unittest.TestCase):
    encode = json.c_encode

class PyJSONEncodingTests(JSONEncodingTests, unittest.TestCase):
    encode = json.py_encode