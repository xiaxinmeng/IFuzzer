class BrowserCookie(BaseCookie):

    def set(self, key, val, coded_val, LegalChars=_LegalChars+':'):
        super().set(key, val, coded_val, LegalChars)