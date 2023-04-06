import requests

with requests.Session() as s:
    cookies = dict(cookies_are='working')
    m = s.get("http://test.com:8000", cookies=cookies)
    print(m.request.headers)
    m = s.get("http://footest.com:8000", cookies=cookies)
    print(m.request.headers)