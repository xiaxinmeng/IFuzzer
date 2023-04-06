data = ['foobar']*100000
mdX = hashlib.sha1()
for d in data:
    mdX.update(d)
mdY = hashlib.sha1()
mdY.update("".join(data))