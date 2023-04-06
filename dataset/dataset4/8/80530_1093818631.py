import re

s = '[a]'

print(*re.findall(r'\[.*]',s))
[a]