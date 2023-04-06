for field in fields:
    if descriptor := getattr(field, 'descriptor'):
        setattr(cls, field.name, descriptor)
    elif default := getattr(field, 'default'):
        setattr(cls, field.name, default)