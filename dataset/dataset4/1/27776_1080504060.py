ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ctx.options |= 0x4