import urllib.request

class MyOpener(urllib.request.FancyURLopener):
    prompt_user_passwd = lambda x, y, z: ("username", "password")

opener = MyOpener()
page = opener.open("http://riddle.p4x.ch/music")
print(page.readlines())