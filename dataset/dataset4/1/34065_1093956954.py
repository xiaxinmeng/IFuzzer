if self.port == HTTP_PORT:
    self.putheader('Host', self.host)
else:
    self.putheader('Host', "%s:%s" % (self.host, 
self.port))