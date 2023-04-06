with gzip.open('/home/joe/file.txt.gz', 'rb') as f_in:
    with open('/home/joe/file.txt', 'wb') as f_out:
        f_out.writelines(f_in)