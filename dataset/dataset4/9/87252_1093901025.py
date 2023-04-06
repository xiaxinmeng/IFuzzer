import binascii
binascii.a2b_base64(b'aGVsbG8=')       # b'hello' (valid)
binascii.a2b_base64(b'aGVsbG8==')      # b'hello' (ignoring data)
binascii.a2b_base64(b'aGVsbG8=python') # b'hello' (ignoring data)