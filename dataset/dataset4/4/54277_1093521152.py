import sys
import second 

if 'second' in sys.modules:
  print ('in sys modules')
  del sys.modules['second']