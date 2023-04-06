def OptionalEnum(value):
    "could also be OptionalEnum(enum, value)"
    try:
        return SomeEnum(value) # or return enum(value)
    except ValueError:
        return value