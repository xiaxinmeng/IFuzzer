with zipfile.ZipFile(archive) as z:
    data = b''
    with z.open(filename, 'rU') as f:
        for line in f:
      	    data += line