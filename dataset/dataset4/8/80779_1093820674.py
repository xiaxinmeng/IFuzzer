if effect is not None:
    if _is_exception(effect):
        raise effect
    elif not _callable(effect):
        result = next(effect)
        if _is_exception(result):
            raise result
    else:
        result = effect(*args, **kwargs)

    if result is not DEFAULT:
        return result