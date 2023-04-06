ready = []
for fd, flags in pollster.poll(timeout):
    obj = map.get(fd)
    if obj:
        ready.append(obj, flags)