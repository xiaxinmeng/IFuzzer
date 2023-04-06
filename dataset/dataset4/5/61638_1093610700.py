def filehash(filepath):
    blocksize = 64*1024
    sha = hashlib.sha256()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()