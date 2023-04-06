from urllib.request import urlopen

import os

web = "http://www.example.org"

open_url = urlopen(web)
fd = open_url.fileno()
with os.fdopen(fd, 'rb') as f:
    file_read_len = len(f.read())

req = urlopen(web)
res_len = len(req.read())