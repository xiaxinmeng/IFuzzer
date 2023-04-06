class C():
    def __iter__(s):
        print('in iter')
        return iter([])
    def __getitem(s,i):
        print('in getitem')

print(1 in C())