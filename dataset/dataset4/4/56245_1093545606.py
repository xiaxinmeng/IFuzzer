import os
from ConfigParser import ConfigParser
from pprint import pprint
c = ConfigParser()
c.read(['test.ini'])
pprint(c.items('test', raw=False, vars=os.environ))