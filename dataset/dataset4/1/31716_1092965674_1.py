def get_overloads(func):
    f = getattr(func, "__func__", func)
    return list(_overload_registry[f.__module__][f.__qualname__].values())