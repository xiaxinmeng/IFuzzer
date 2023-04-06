@contextmanager
def nested_empty():
    yield []

@contextmanager
def nested_append(prev, next):
    with prev as a, next as b:
        a.append(b)
        yield a

def nested(*managers):
    total = nested_empty()
    for mgr in managers:
        total = nested_append(total, mgr)
    return total