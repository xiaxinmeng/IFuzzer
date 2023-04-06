import os
import urllib.request
import encodings.idna

os.chroot("/tmp")

urllib.request.urlopen("http://localhost")