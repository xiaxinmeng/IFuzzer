class ParseArgumentsTestCase(unittest.TestCase):
    def test_no_arguments(self):  # type: () -> None
        with self.assertRaises(SystemExit):
            # Suppress argparse stderr.
            class NullWriter:
                def write(self, s):  # type: (str) -> None
                    pass

            sys.stderr = NullWriter()
            parse_arguments()