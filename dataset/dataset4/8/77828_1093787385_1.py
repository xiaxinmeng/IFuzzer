import re

s = 'this is my string'
subs = {'my': 'your', 'string': 'car'}
print(re.sub('|'.join(subs), lambda m: subs[m.group(0)], s))