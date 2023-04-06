from urllib import request
from time import sleep
while True:
    req = request.Request('https://www.python.org/')
    request.urlopen(req)
    sleep(1)