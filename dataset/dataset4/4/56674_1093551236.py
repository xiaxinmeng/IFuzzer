import gc
gc.get_referents(object.__dict__)[0].clear()
gc.get_referents(type.__dict__)[0].clear()
type("A", (), {})()