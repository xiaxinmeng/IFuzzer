def msg_callback(conn, direction, version, content_type, msg_type, data):
    if direction == 'read' and b'acme-tls/1' in data:
        print('got an acme-tls/1 request')
        print('set a flag for sni_callback to check, etc etc')