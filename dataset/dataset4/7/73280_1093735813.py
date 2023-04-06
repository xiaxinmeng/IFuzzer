from zipfile import ZipFile
with open('a.zip', 'wb') as base:
    base.write(b'old\n')
    with ZipFile(base, 'a') as myzip:
        myzip.write('eggs.txt')