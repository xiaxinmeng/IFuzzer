def public(api):
    sys.modules[api.__module__].__all__.append(api.__name__)
    return api

__all__ = list()
@public
def public_function(): ...
@public
class PublicClass: ...