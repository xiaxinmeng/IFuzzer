def _asdict_inner(obj, dict_factory):
    if _is_dataclass_instance(obj):
        return getattr(obj, _PARAMS).asdict(obj) 