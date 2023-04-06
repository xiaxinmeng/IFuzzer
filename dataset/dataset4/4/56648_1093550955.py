self.send_response(response.status)
for name, value in response.getheaders():
    self.send_header(name, value)
self.end_headers()