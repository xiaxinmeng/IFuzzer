import os
import urllib.request

os.chroot("/tmp")

urllib.request.urlopen("http://localhost")