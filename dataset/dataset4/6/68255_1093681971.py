import collections
import weakref

class NotIterator:
    pass

not_iterator = NotIterator()
isinstance(not_iterator, collections.Iterator) # returns False

proxy_object = weakref.proxy(not_iterator)
isinstance(proxy_object, collections.Iterator) # returns True, should be False