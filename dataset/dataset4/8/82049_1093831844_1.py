def _is_dataclass_instance(obj):
    return hasattr(type(obj), _FIELDS)