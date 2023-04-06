import marshal
s = 'c' + ('X' * 4*4) + '{' * 2**20
marshal.loads(s)