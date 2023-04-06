import marshal, dis
pyc = open('bados.pyc', 'rb').read()
code = marshal.loads(pyc[8:])
dis.dis(code)