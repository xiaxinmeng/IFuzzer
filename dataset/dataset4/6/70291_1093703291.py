def has_data_descriptor_attrs(obj):
    return set(['__set__', '__delete__']) & set(dir(obj))

def is_data_descriptor(obj):
    return bool(has_data_descriptor_attrs(obj))