class MyHTTPPasswordMgr(urllib.request.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        return "a", "b"