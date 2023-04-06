import pathlib
def pathread(self, binary=False):
    with self.open('br'if binary else 'r') as fread:
        return fread.read()

def pathwrite(self, data, mode='w'):
    with self.open(mode) as fwrite:
        fwrite.write(data)

		
pathlib.Path.read = pathread
pathlib.Path.write = pathwrite
p = pathlib.Path('/mydir/example.txt')
p.read()
# 'Content from path.\n'

p.write('I am appending.\n', mode='a')
p.read()
# 'Content from path.\nI am appending.\n'