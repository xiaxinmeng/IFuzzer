zf = zipfile.ZipFile('a.zip')
memf = zf.open('abc/def/1.txt', 'r')
zf2 = zipfile.ZipFile(memf) 