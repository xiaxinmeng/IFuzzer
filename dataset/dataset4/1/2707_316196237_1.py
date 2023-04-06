for obj in r:
    if obj.fileno() is not None:
        _read(obj)

for obj in w:
    if obj.fileno() is not None:
        _write(obj)

for obj in e:
    if obj.fileno() is not None:
        _exception(obj)