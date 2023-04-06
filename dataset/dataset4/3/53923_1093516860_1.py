class DigestAuthHandler (urllib2.HTTPDigestAuthHandler):
    def get_authorization (self, req, chal):
        qop = chal.get ('qop', None)
        if qop and ',' in qop and 'auth' in qop.split (','):
            chal['qop'] = 'auth'

        return urllib2.HTTPDigestAuthHandler.get_authorization (self, req, chal)