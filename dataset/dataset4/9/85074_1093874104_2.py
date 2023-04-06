def monkey_patch_typing() -> None:
    import inspect, typing
    def _signature_get_user_defined_method(cls, method_name):
        try:
            meth = getattr(cls, method_name)
        except AttributeError:
            return
        else:
            if meth in (typing.Generic.__new__, typing.Protocol.__new__):
                # Exclude methods from the typing module.
                return

            if not isinstance(meth, inspect._NonUserDefinedCallables):
                # Once '__signature__' will be added to 'C'-level
                # callables, this check won't be necessary
                return meth

    inspect._signature_get_user_defined_method = _signature_get_user_defined_method

monkey_patch_typing()