zf = zipfile.ZipFile('a.zip')
memf = zf.open('abc/def/1.zip', 'r')
zf2 = zipfile.ZipFile(memf) 