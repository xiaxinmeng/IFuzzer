def ob():
   print('ob fetched')
   return d

def key():
   print('key called')
   return 0

d = [[]]
ob()[key()] += [1]
print(d)