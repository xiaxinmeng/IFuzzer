
import sys
sys.modules.pop('stat', None)
sys.modules['_stat'] = None
import stat
print(stat.S_ISDOOR(123))
