from urllib.request import *

opener = FancyURLopener()
opener.retrieve("http://username:password@google.com/index.html", "index.html")