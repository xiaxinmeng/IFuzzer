import zipfile
zf = zipfile.ZipFile('out.xxx.zip', 'r')
f = zf.open('out.xxx')
r = "x" * (1024*1024*20)
f.readline()
r = ""