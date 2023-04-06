from urllib.request import Request
from http.cookiejar import Cookie, CookieJar

jar = CookieJar()
jar.set_cookie(Cookie(
            None, 'test', 'test',
            None, False,
            '.test.com', True, False,
            '/', True,
            False, None, False, None, None, None
        ))
r = Request('http://www.test.com')
jar.add_cookie_header(r)