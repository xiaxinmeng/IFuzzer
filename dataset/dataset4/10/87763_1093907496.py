
def read(self, sslcontext=None):
    """Reads the robots.txt URL and feeds it to the parser."""
    try:
        if sslcontext:
           f = urllib.request.urlopen(self.url, context=sslcontext)
        else:
           f = urllib.request.urlopen(self.url)
    except urllib.error.HTTPError as err:
        if err.code in (401, 403):
            self.disallow_all = True
        elif err.code >= 400 and err.code < 500:
            self.allow_all = True
    else:
        raw = f.read()
        self.parse(raw.decode("utf-8").splitlines())

