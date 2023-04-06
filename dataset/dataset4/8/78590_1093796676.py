def dataclass_asdict(obj, dict_factory):
    result = []
    for f in fields(obj):
        value = _asdict_inner(getattr(obj, f.name), dict_factory)
        result.append((f.name, value))
    return dict_factory(result)