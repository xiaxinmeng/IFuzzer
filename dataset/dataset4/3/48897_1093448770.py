class RoundtripLegalSyntaxTestCase(unittest.TestCase):

    def test_relative_import_statement(self):
        self.check_suite("from . import sys")