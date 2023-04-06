with zipfile.ZipFile('foo.zip') as file:
    for name in ['file-1.txt', 'file-2.txt']:
        p = zipfile.Path(file, name)
        with p.open() as inner:
            print(list(inner)) # ValueError: seek of closed file