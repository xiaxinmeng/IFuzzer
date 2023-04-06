import sys
print(sys.stdout)
import os
print([(k, os.environ[k]) for k in os.environ if k.startswith('LC')])
print([(k, os.environ[k]) for k in os.environ if k.startswith('LANG')])
import locale
print(locale.getlocale())
print('\u00e5')
print('\u0061\u030a')