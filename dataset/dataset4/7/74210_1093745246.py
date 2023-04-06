import sys

import mytest.mod1
assert 'mytest.mod1' in sys.modules
import mytest.mod1 as mod  # this fails, though the prev. lines work perfectly