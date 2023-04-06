pycon
"""
>>> import os
[43913 refs]
>>> os.close(1)
[43913 refs]
>>> input()
1
[43915 refs]
<crash>
"""

"""
>>> import os
[43913 refs]
>>> f = file('test', 'wb')
[43921 refs]
>>> os.close(f.fileno())
[43921 refs]
>>> f.flush()
[43921 refs]
>>> f.write('test')
[43921 refs]
>>> f.flush()
<crash>
"""
