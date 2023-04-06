import urllib3

pool_manager = urllib3.PoolManager()

host = "localhost:7777?a=1 HTTP/1.1\r\nX-injected: header\r\nTEST: 123"
url = "http://" + host + ":8080/test/?test=a"