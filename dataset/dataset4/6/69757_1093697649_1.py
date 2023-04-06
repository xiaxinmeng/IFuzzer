# Were we compiled --with-pydebug or with #define Py_DEBUG?
Py_DEBUG = hasattr(sys, 'gettotalrefcount')