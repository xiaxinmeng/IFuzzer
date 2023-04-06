# pseudo-code, will be in C
_the_registry: Dict[WeakRef[type], Set[WeakRef[type]]] = {}
...
def _abc_register(cls, subcls):
    _registry = _the_registry[ref(cls)]
    _registry.add(ref(subcls))
    return subcls