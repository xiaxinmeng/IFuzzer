class TimeoutTest(unittest.TestCase):
    def test_http_basic(self):
        self.assertIsNone(socket.getdefaulttimeout())
        url = "http://www.example.com"
        with support.transient_internet(url, timeout=None):
            u = _urlopen_with_retry(url)
            self.addCleanup(u.close)
            self.assertIsNone(u.fp.raw._sock.gettimeout())