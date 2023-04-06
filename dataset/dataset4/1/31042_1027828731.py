if isinstance(obj, types.MethodType):
                obj.__func__.__no_type_check__ = True