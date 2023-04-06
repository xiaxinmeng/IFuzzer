with tempfile.NamedTemporaryFile() as f:
    f.write(broken_message.encode())
    f.seek(0)
    msg = mailbox.mbox(f.name)
    for m in msg:
        print(m.get_payload())