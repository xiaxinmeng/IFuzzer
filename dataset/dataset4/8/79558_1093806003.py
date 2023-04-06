urlunsplit(urlsplit("httpbin.org", scheme="https://"))
'https://:httpbin.org'

urlunsplit(urlsplit("httpbin.org", scheme="https"))
'https:///httpbin.org'