with gzip.open('/home/joe/file.txt.gz', 'rb') as f_in:
    with open('/home/joe/file.txt', 'wb') as f_out:
        while True:
            c = f_in.read(chunk_size)
            if not c: break
            d = f_out.write(c)