#
# Note: to trigger a crash reliably, the debugging code in gc_list_remove
#       _must_ be turned on.
#
import gc
gc.set_threshold(1)

class Node:
   
   def __del__(self):
      dir(self)
 
a = Node()
del a # -> Crash