if not hasattr(threading.current_thread(), "_children"):
    threading.current_thread()._children = weakref.WeakKeyDictionary()