class HTTPBasicAuthHandlerF(AbstractBasicAuthHandler,
BaseHandler):

    auth_header = 'Authorization'

    def http_error_401(self, req, fp, code, msg, headers):
        host = req.get_full_url()
        return self.http_error_auth_reqed('www-authenticate',
                                          host, req, headers)