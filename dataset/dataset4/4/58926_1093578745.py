import http.client
conn = http.client.HTTPConnection('localhost',8888)
conn.request("POST", "/post", "", {})
conn.close()