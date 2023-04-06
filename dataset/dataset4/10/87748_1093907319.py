def alpn_cb(sslsocket, client_alpn_protocols, negotiated):
    return negotiated

context.alpn_cb = alpn_cb