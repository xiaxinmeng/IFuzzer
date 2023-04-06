out = self.get_output('-X', utf8_opt, '-c', code, arg, **kw)
becomes
out = self.get_output('-X', utf8_opt, '-c', code, 'h\xe9\u20ac'.encode('utf-8'), **kw)
becomes
out = self.get_output('-X', utf8_opt, '-c', code, b'h\xc3\xa9\xe2\x82\xac', **kw)