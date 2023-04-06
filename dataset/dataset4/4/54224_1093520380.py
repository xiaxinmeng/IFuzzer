if not hasattr(threading.current_process(), "_children"):
    threading.current_process()._children = weakref.WeakKeyDictionary()