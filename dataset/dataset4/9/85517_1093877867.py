import requests
from time import sleep

import logging
logging.basicConfig(level=logging.DEBUG)

s = requests.Session()
s.verify = False  # self-signed cert

counter = 0
txt = "test"
while True:
    counter = counter + 1
    s.post('http://localhost', data={counter:txt})
    sleep(5)