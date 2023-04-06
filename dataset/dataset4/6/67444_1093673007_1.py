def redirect(self, url, status=http.HTTPStatus.FOUND):
    self.send_response(status)
    self.send_header('Location', url)
    self.end_headers()