def cert_verify_callback(sslsocket, storectx, verify_ok):
    context = sslsocket.context