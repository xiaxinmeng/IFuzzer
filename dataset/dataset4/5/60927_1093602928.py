import urllib.request
import io

url = "http://www.python.org"
handle = urllib.request.urlopen(url)
wrapped_handle = io.TextIOWrapper(handle, encoding='utf-8')
for line in wrapped_handle:
    pass