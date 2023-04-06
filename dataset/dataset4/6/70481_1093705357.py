from zipfile import ZipFile
with open('a.zipp', 'wb') as base:
    base.write(b'old\n')
    with ZipFile(base, 'a') as myzip:
        myzip.write('eggs.txt')