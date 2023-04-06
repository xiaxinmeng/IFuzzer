from urllib.request import urlopen
with urlopen("http://localhost:8000") as response:
    response.read()
import gc; gc.collect()