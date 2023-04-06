res = PyObject_CallFunction(func, NULL);
res = PyObject_CallFunctionObjArgs(func, NULL);
res = _PyObject_CallNoArg(func)   # private