class S(str):

    def __eq__(self, other):
        d.clear()
        return NotImplemented

    def __hash__(self):
        return hash('test')

d = {S(): 'value'}
'test' in d