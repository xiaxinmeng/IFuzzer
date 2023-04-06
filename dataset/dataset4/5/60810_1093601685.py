with open(file, "rb") as f:
    while True:
        data = f.read(16384)
        if not data:
            break
        myhash.update(data)