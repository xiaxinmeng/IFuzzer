s = ('u%s:%s' % self.credentials).encode('utf-8')

s = 'Basic ' + base64.b64encode(s).strip()