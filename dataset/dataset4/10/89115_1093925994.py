items = ['a', '', 'b', '', 'c', '', 'd', '', 'e', '']

print(len(items))

for index, item in enumerate(items):
    print(index, repr(item), items)
    if item == '':
        items.remove('')