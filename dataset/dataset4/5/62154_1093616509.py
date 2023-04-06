class EnumMeta():
    allow_subclass = False


class MyEnumMeta(EnumMeta):
    allow_subclass = True