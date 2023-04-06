chunk_size = 1024
with open('/home/joe/file.txt', 'rb') as f_in:
    with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
        while True:
            c = f_in.read(chunk_size)
            if not c: break
            d = f_out.write(c)