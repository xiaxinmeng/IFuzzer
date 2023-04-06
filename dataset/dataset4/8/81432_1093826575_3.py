def _is_async_obj(obj):
    code = getattr(obj, '__code__', None)
    if code and not isinstance(code, CodeType):
        return False
    return asyncio.iscoroutinefunction(obj) or inspect.isawaitable(obj)