def PyObject_LookupSpecial(obj, name):
    tp = type(obj)
    try:
        return getattr(tp, name)
    except AttributeError:
        return getattr(tp.tp_proxy(), name)