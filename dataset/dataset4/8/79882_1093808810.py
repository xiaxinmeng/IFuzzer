x = uuid.uuid4()
y = weakref.ref(x)
assert x is y()