import sys
from os import path
sys.path.append(path.abspath('ab'))
sys.path.append(path.abspath('ac'))

from a.b import api as api_ab
from a.c import api as api_ac