import ssl
context = ssl.create_default_context()
context.set_npn_protocols(['http/1.1', 'spdy/2'])