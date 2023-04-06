class MyClassManager(UManager):
    def __reduce__(self):
        return (RebuildMyClassManager,
                (self._address, None, self._serializer))
WorkCounterManager.register('MyClass', MyClass, MyClassProxy)
#optionally: WorkCounterManager.register('_MyClass', None, MyClassProxy, create_method=False)

def RebuildMyClassManager(address, authkey, serializer):
    mgr = MyClassManager(address, authkey, serializer)
    mgr.connect()
    return mgr