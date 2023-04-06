# copy this to test.py
# > touch foo.txt
# > python3.1 -c "import test; import collections"
# > ...
# >   File "test.py", line 5, in find_module
# >     def find_module(self, mname, path = None): open("foo.txt")
# >   File "test.py", line 5, in find_module
# >     def find_module(self, mname, path = None): open("foo.txt")
# >   File "test.py", line 5, in find_module
# >     def find_module(self, mname, path = None): open("foo.txt")
# >   File "test.py", line 5, in find_module
# >     def find_module(self, mname, path = None): open("foo.txt")
# > RuntimeError: maximum recursion depth exceeded while calling a
# > Python object
class importer(object):
  def find_module(self, mname, path = None): open("foo.txt")
import sys; sys.meta_path.append(importer)