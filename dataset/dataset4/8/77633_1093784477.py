import warnings

if cls.__dataclass_params__.init:
    for pcls in cls.mro():
        if pcls.__init__ is not object.__init__:
            try:
                d_params = getattr(pcls, "__dataclass_params__")
            except AttributeError:
                warnings.warn('Found a not called init')
            else:
                if not d_params.init:
                    warnings.warn('Found a custom dataclass init')