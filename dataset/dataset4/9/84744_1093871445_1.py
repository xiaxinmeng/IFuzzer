with zipfile.ZipFile('foo.zip') as file:
    for name in ['file-1.txt', 'file-2.txt']:
        with file.open(name) as inner:
            print(list(inner)) # Works!