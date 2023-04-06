# note recursion behavior stops if we don't call open()
class importer(object):
  def find_module(self, mname, path = None): pass
import sys; sys.meta_path.append(importer)