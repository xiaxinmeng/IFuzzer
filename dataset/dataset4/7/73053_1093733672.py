
import tempfile
import unittest


class MyTest(unittest.TestCase):
    def test_temporary_file(self):
        tempfile.TemporaryFile()

    def test_named_temporary_file(self):
        tempfile.NamedTemporaryFile()
