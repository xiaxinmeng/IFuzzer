import gc; gc.set_threshold(5)
import sys

old_modules = dict(sys.modules)
sys.modules.clear()
sys.modules.update(old_modules)

import _ast
import gc
gc.collect()