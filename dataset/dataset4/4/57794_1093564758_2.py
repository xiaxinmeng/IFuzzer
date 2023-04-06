with ContextManager() as mgr:
    foo = ctxtmgr()
    mgr.register(foo.__close__)