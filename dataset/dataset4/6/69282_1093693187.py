def do_GET(self):
    self.send_response(HTTPStatus.OK)
    self.end_headers()
    self.close_connection = True  # Terminate response body to proxy