conn = HTTPSConnection(server,port)
conn.connect()
conn.request('POST', '/', data, headers)