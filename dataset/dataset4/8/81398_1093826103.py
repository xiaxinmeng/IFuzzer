hostname = "www.xn--b.buchhandlunggründen.de"

ctx = ssl.create_default_context()
s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
s.check_hostname = True
try:
    s.connect((hostname, 443))
except UnicodeError as incorrect_punycode:
    pass