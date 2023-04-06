myList = []
for item in myList:
    print( item ) # <<< works

for item in myList.reverse(): # <<< breaks with: TypeError: 'NoneType' object is not iterable
    print( item ) #