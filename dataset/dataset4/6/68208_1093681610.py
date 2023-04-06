CONTEXT = None

class MyFUSE(Fuse):

   def __call__(self, op, path, *args):
      global CONTEXT
      ...
      CONTEXT = threading.local()
      # set several CONTEXT vars
      ...
      # dispatch to correct function to handle 'op'