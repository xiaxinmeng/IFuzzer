def test_url_cleanup_opener(self):
    url = 'http://docs.python.org/library/urllib.html'
    self.fakehttp(b"HTTP/1.1 200 OK\r\n\r\nHello!")
    try:
        fp = urllib.request.urlopen(url)
        self.assertIsInstance(urllib.request._opener, urllib.request.OpenerDirector)
        urllib.request.urlcleanup()
        self.assertIsNone(urllib.request._opener)
    finally:
        self.unfakehttp()