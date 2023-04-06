import re
r=re.compile(r"(?P<alpha>...)")

while 1:
  mo=r.match("blabla")
  mo.groupdict()