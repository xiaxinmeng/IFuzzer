
import locale
import re

locale.setlocale(locale.LC_CTYPE, 'en_US.utf8')
print(re.match(b'\xc5', b'\xe5', re.L|re.I))
