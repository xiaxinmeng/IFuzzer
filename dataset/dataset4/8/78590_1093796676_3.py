def _asdict_inner(obj, dict_factory):
    if _is_dataclass_instance(obj):
        if getattr(obj, _PARAMS).directly_serializable: 
            return dict_factory(obj)