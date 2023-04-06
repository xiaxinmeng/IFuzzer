def test_alwayspath(self):
    u = urlparse.urlparse("http://netloc/path;params?query#fragment")
    self.assertEqual(urlparse.urlunparse(u),
"http://netloc/path;params?query#fragment")

    u = urlparse.urlparse("http://netloc?query#fragment")
    self.assertEqual(urlparse.urlunparse(u),
"http://netloc/?query#fragment")

    u = urlparse.urlparse("http://netloc#fragment")
    self.assertEqual(urlparse.urlunparse(u), "http://netloc/#fragment")