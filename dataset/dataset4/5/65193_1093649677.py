ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ctx.options &= ~ssl.OP_NO_COMPRESSION