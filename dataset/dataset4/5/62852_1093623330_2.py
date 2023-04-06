import re

from first import first


re1 = re.compile('b(.*)')
re2 = re.compile('a(.*)')

m = first(regexp.match('abc') for regexp in [re1, re2])
if not m:
   print('no match!')
elif m.re is re1:
   print('re1', m.group(1))
elif m.re is re2:
   print('re2', m.group(1))