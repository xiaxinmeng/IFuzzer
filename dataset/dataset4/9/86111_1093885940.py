http_cookie = 'id=12345; [object Object]=data; something=not_loaded'
for cookie_key in http_cookie.split(';'):
  c.load(cookie_key)