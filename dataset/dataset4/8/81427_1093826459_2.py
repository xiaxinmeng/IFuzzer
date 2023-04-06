req = Request("https://example.com")
policy1 = DefaultCookiePolicy()
print(policy1.return_ok(cookie, req))