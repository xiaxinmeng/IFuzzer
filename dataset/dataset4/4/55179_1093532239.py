import hmac
import hashlib
import base64


signature = hmac.new('secret', 'url', hashlib.sha512).digest()
assert signature.encode('base64') == base64.b64encode(signature)