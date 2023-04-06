client_ciphers = {'AES128-SHA256', 'AES256-SHA256'}
server_ciphers = {'AES256-SHA256', 'AES128-SHA'}
shared_ciphers = {'AES128-SHA256', 'AES256-SHA256'}  # SSL_get_client_ciphers()
shared_ciphers = {'AES256-SHA256', 'AES128-SHA'}  # SSL_get_ciphers()