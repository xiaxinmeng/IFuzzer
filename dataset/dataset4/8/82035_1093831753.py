
from urllib.parse import urlparse

url = "http://us#er:123@localhost:9001/RPC2"
u = urlparse(url)
print(u)
# ParseResult(scheme='http', netloc='us', path='', params='', query='', fragment='er:123@localhost:9001/RPC2')
