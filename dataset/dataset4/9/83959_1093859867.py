
import collections
import gc
import weakref

hooks_dict = collections.OrderedDict()
hooks_dict_ref = weakref.ref(hooks_dict)
gc.collect()

print('Hello world')
