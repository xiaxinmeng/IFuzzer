@unittest.skipUnless(sys.platform == "win32", "Win32 specific tests")
class Win32APITests(unittest.TestCase):

    def test_dword_convert_negative(self):
        with self.assertRaises(ValueError):
            for h in _winapi.CreatePipe(None, -1):
                _winapi.CloseHandle(h)

    def test_dword_convert_overflow(self):
        with self.assertRaises(OverflowError):
            for h in _winapi.CreatePipe(None, 1 << 32):
                _winapi.CloseHandle(h)