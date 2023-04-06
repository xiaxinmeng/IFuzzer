import urllib.parse

urls = ("https://example.com/test?foo=foo&bar=bar", "https://example.com/test?foo=foo;bar=bar")
for url in urls:
    urllib.parse.parse_qsl(url)  # this is forced to support both