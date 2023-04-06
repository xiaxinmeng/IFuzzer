class Response(object):
    """
    Take a httplib2 response and turn it into a requests response
    """
    def __init__(self, httplib_resp, content, url, http_obj):
        self.content = content
        self.cached = False
        self.status_code = int(httplib_resp.status)
        self.ok = self.status_code < 400
        self.url = url
        self.connections = http_obj.connections