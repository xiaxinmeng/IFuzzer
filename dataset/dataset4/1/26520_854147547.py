
# Expect either an SSL error about the server rejecting
# the connection, or a low-level connection reset (which
# sometimes happens on Windows)
s.connect((HOST, server.port))
