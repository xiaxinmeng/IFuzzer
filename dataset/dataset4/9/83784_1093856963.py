def request(self, method, url, body=None, headers={}, *,          
            encode_chunked=False):                                
    """Send a complete request to the server."""                  
    self._send_request(method, url, body, headers, encode_chunked)