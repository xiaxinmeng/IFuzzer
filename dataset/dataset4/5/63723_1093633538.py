from urllib.request import urlopen
with urlopen("http://localhost") as response: response.read()