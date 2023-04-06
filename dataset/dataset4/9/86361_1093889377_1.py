def copy_with(self, params):
    return _CallableGenericAlias(self.__origin__, params,
                                 name=self._name, inst=self._inst)