class ImmortalType(type, metaclass=BoringType): pass

ImmortalType.__class__ = ImmortalType
gc.collect()
del BoringType
gc.collect()
del ImmortalType
gc.collect()