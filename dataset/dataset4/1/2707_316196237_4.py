for obj, flags in ready:
    if obj.fileno() is not None:
        readwrite(obj, flags)