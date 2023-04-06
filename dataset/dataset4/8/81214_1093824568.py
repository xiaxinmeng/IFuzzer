def deflt(x):
    print('\nKey', x, 'is not in the dictionary')
    return 'Default'

dicti = {1:'one', 2:'two', 3:'three'}

key = 2
print('\ndicti \t\t', dicti)
print('\t\t key =',key)

print('get \t\t',     dicti.get(key, deflt(key)))
print('setdefault \t',dicti.setdefault(key, deflt(key)))
print('dicti \t\t',   dicti)
print('pop \t\t',     dicti.pop(key, deflt(key)))
print('dicti \t\t',   dicti)
print('setdefault \t',dicti.setdefault(key, deflt(key)))
print('dicti \t\t',   dicti)