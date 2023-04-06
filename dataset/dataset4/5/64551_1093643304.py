class adminpopserver(poplib.POP3):
    def auth(self, method, secret):
        return self._shortcmd('AUTH %s %s' % (method, secret))

secret = "{user}\0{adminuser}\0{password}".format(
    user=user, 
    adminuser=adminuser, 
    password=password)
secret = secret.encode('base64').strip('\n')