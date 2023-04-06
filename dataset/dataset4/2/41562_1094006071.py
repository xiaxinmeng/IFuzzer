pycon
"""
>>> p.StreamURL1.value
'mss://stream.url'
>>> p.StreamURL2.src

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in -toplevel-
    p.StreamURL2.src
  File "C:\Python24\Lib\site-packages\segfault240\PyMeld.
py", line 475, in __getattr__
    start = self._findElementFromID(name)
  File "C:\Python24\Lib\site-packages\segfault240\PyMeld.
py", line 425, in _findElementFromID
    match = _findIDMatch(nodeID, subset)
  File "C:\Python24\Lib\site-packages\segfault240\PyMeld.
py", line 282, in _findIDMatch
    match = re.search(thisRE, text)
  File "C:\Python24\lib\sre.py", line 134, in search
    return _compile(pattern, flags).search(string)
MemoryError
>>> 
"""
