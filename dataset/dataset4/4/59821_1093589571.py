import logging
import logging.handlers
from pprint import pprint
import yaml

# Option 1 - OK
h1 = logging.handlers.RotatingFileHandler(filename = "test.log", maxBytes = 262144, backupCount = 3)
h2 = yaml.load("""
!!python/object/new:logging.handlers.RotatingFileHandler
    kwds:
        filename: test.log
        maxBytes: 262144
        backupCount: 3
""")
h3 = logging.FileHandler('test.log')
h4 = yaml.load("""
!!python/object/new:logging.FileHandler
    kwds:
        filename: test.log
""")

print('RotatingFileHandler using code: %s' % type(h1))
pprint(h1.__dict__)
print('RotatingFileHandler using YAML: %s' % type(h2))
pprint(h2.__dict__)
print('FileHandler using code: %s' % type(h3))
pprint(h3.__dict__)
print('FileHandler using YAML: %s' % type(h4))
pprint(h4.__dict__)