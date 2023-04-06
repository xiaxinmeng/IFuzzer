def setUp(self):
    socket.setdefaulttimeout(self.TIMEOUT)

def testURLread(self):
    f = _open_with_retry(urllib.urlopen, "http://www.example.com/")
    x = f.read()  # Timed out!