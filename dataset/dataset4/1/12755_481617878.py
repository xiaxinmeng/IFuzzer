
with contextlib.closing(http.client.HTTPConnection(ADDR, PORT)) as conn:
    conn.request('POST', '/RPC2 HTTP/1.0\r\nContent-Length: 100\r\n\r\nbye')
