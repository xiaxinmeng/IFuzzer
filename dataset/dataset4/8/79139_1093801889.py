
from urllib.error import HTTPError
from urllib.request import urlopen

def make_request():
    try:
        urlopen('https://httpbin.org/status/418')
        assert False
    except HTTPError as err:
        assert err.code == 418
        return err.fp

fp = make_request()
assert fp.isclosed()  # Fails on Windows, passes on other platforms
