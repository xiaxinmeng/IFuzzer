zf = zipfile.ZipFile(...)
for name in zf.namelist():
    stream = zf.open(name)
    data = stream.read()
    stream.close()
    with open(name.replace(...), "w") as stream:
        stream.write(data)