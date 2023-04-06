import re

r = re.compile(re.escape('/foo'))
print(r)
print(r.pattern)
assert r.pattern.startswith('\\/')