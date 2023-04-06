with open('email.eml', 'rb') as f:
    msg = email.message_from_binary_file(f, policy=default)
    toheader = msg['To']
    for addr in toheader.addresses:
        print(addr)