class Table:
    def __getitem__(self, key):
        if key == 99:   raise LookupError() #'c'
        elif key == 100: return None  # 'd'
        elif key == 101: return 'xyz'  # 'e'
        else: return key+1
                
print('abcdef'.translate(Table()))
# bccxyzg