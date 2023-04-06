from datetime import datetime
s = '20160505 160000'
try:
    refdatim = datetime.strptime(s, '%Y%m%d %H%M%S')
except TypeError:
    import time
    refdatim = datetime.fromtimestamp(time.mktime(time.strptime(s, '%Y%m%d %H%M%S')))
