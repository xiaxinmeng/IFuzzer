import urllib
from http.cookiejar import DefaultCookiePolicy

policy = DefaultCookiePolicy()
req = urllib.request.Request('https://xxxfoo.co.jp/')
print(policy.domain_return_ok('foo.co.jp', req))