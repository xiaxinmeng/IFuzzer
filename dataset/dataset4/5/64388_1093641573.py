pytb
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "P:\ath\to\cpython\lib\_sitebuiltins.py", line 99, in __call__
    return pydoc.help(*args, **kwds)
  File "P:\ath\to\cpython\lib\pydoc.py", line 1792, in __call__
    self.help(request)
  File "P:\ath\to\cpython\lib\pydoc.py", line 1842, in help
    else: doc(request, 'Help on %s:', output=self._output)
  File "P:\ath\to\cpython\lib\pydoc.py", line 1578, in doc
    pager(render_doc(thing, title, forceload))
  File "P:\ath\to\cpython\lib\pydoc.py", line 1571, in render_doc
    return title % desc + '\n\n' + renderer.document(object, name)
  File "P:\ath\to\cpython\lib\pydoc.py", line 356, in document
    if inspect.ismodule(object): return self.docmodule(*args)
  File "P:\ath\to\cpython\lib\pydoc.py", line 1142, in docmodule
    contents.append(self.document(value, key, name))
  File "P:\ath\to\cpython\lib\pydoc.py", line 358, in document
    if inspect.isroutine(object): return self.docroutine(*args)
  File "P:\ath\to\cpython\lib\pydoc.py", line 1323, in docroutine
    signature = inspect.signature(object)
  File "P:\ath\to\cpython\lib\inspect.py", line 1551, in signature
    raise ValueError(msg)
ValueError: no signature found for builtin function <built-in function abort>
"""
