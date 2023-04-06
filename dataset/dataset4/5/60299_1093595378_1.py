class MyHTTPPasswordMgr(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        return "a", "b"