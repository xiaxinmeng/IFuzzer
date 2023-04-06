import BaseHTTPServer

def _bare_address_string(self):
    host, port = self.client_address[:2]
    return '%s' % host