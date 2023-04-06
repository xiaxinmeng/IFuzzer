import logging

f = logging.StrFormatStyle('{asctimer}')
print(f.usesTime())
f = logging.PercentStyle('%(astimer)s')
print(f.usesTime())