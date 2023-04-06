class MiscTestCase(unittest.TestCase):
    def test_without_join(self):
        # Test that a thread without join does not leak references.
        # Use a debug build and run "python -m test -R: test_threading"
        threading.Thread().start()