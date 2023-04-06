from __future__ import print_function
S = []

def l(c):
  for i in [0,1]:
    S.append(c)
    yield i
  S.append(c.upper())

la = l('a')
lb = l('b')

for a,b in zip(la, lb):
  S.append("#")
print(''.join(S))