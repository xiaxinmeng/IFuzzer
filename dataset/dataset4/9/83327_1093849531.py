import re
import time
NON_PRINTABLE = re.compile(u'[^\U00010000-\U0010ffff]')
time.sleep( 30 )