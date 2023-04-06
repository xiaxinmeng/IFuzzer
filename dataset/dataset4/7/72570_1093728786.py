import hmac, hashlib

h = hmac.HMAC(b'secret', digestmod=hashlib.shake_256)
h.hexdigest() # raises on self.inner.digest() requires length argument