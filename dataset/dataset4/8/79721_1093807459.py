if isinstance(obj, dict):
    new_keys = tuple((_asdict_inner(k, dict_factory),
                      _asdict_inner(v, dict_factory))
                      for k, v in obj.items())