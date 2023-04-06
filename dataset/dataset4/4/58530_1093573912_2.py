
class myHMAC(hmac.HMAC):
    blocksize = 1
    def __init__(self, key, msg, digestmod_):
        super().__init__(key, msg, digestmod=digestmod_)

h = myHMAC(b"key", b"", digestmod_="md5")
h.digest() # <- works perfectly fine.
