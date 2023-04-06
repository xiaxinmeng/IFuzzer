import io
import urllib.request

f_bytes = urllib.request.urlopen("http://www.python.org/")
f_string = io.TextIOWrapper(f_bytes, "iso-8859-1")
print(f_string.read())