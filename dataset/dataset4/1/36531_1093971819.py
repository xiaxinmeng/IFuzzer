PySocketSock_Type.tp_getattro = PyObject_GenericGetAttr;
PySocketSock_Type.tp_alloc = PyType_GenericAlloc;
PySocketSock_Type.tp_free = PyObject_Del;