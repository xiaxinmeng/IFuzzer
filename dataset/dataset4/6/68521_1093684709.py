import urllib.request


class SimplePasswordManager(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_password(self, realm, uri, user, passwd):
        pass

    def find_user_password(self, realm, authuri):
        return self.username, self.password


proxy_handler = urllib.request.ProxyHandler({
    'http': '<proxy server ip>',
    'https': '<proxy server ip>',
})
password_mgr = SimplePasswordManager('<username>', '<password>')
proxy_auth_handler = urllib.request.ProxyDigestAuthHandler(passwd=password_mgr)
opener = urllib.request.build_opener(proxy_auth_handler, proxy_handler)
req = opener.open('http://httpbin.org/ip')
print(req.read().decode('ascii'))
req = opener.open('https://httpbin.org/ip')
print(req.read().decode('ascii'))