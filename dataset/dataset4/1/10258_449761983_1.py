pol.set_blocked_domains([])
req = urllib.request.Request("http://acme.com/")
res = FakeResponse(headers, "http://acme.com/")
cookies = c.make_cookies(res, req)
c.extract_cookies(res, req)
self.assertEqual(len(c), 1)

print(cookies[0]) # <Cookie CUSTOMER=WILE_E_COYOTE for acme.com/>
req = urllib.request.Request("http://badacme.com/")
self.assertFalse(pol.return_ok(cookies[0], req)) # This fails returning true though cookie is set on acme.com