#a.py
from .b import util

#b.py
from .util import util

#b/util.py
from .. import a
def util(): pass

#__main__.py
import b