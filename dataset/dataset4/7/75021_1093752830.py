import unicodedata
import re
import sys

cre = re.compile(r'\w')

for cp in range(sys.maxunicode + 1):
    s = chr(cp)

    if s.isidentifier() and not cre.match(s):
        print(hex(cp), unicodedata.name(s))