for field in fields:
    if (
        (descriptor := getattr(field, 'descriptor'))
        and (default := getattr(field, 'default'))
    ):
        setattr(self, field.name, default)
    elif default_factory := getattr(field, 'default_factory'):
        setattr(self, field.name, default_factory())