reader, writer = await asyncio.open_connection(
    *addr,
    ssl=client_sslctx,
    server_hostname='',
    loop=self.loop,
    ssl_handshake_timeout=1.0)

# we will get to this line without an error even if
# SSL handshake failed and the connection is
# in a semi-closed state.  o_O
print('HERE')