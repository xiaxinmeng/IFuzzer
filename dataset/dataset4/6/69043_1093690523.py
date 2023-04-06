
from unittest.mock import patch
import urllib
from urllib import request
from urllib.request import urlopen

@patch('urllib.request.urlopen')
def openPatch(urlopenMock):
    print(urlopenMock)
    print(urlopen)
    print(request.urlopen)
    print(urllib.request.urlopen)

openPatch()
