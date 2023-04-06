class BasicAuthTests(unittest.TestCase):
    ...

    def test_basic_auth_success(self):
        ...
        try:
            self.assertTrue(urllib.request.urlopen(self.server_url))
        except urllib.error.HTTPError:
            self.fail("Basic auth failed for the url: %s", self.server_url)