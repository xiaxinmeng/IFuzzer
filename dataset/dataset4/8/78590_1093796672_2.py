def root_dataclass_dict_factory(obj):
    if isinstance(obj, list):
        dataclass_dict = dict(obj)
        if 'options' in dataclass_dict:
            dataclass_dict.update(dataclass_dict.pop('options'))

    return dict(obj)