def do_GET(self):
    self.send_response(HTTPStatus.OK)
    self.send_header("Content-Length", "0")  # Stop proxy reading body
    self.end_headers()