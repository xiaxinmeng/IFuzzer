class MyCookieJar(CookieJar):
    def _cookie_from_cookie_tuple(self, tup, request):
        name, value, standard, rest = tup
        standard["version"]= None
        CookieJar._cookie_from_cookie_tuple(self, tup, request)