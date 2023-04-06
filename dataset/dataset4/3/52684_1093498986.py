# register commands
PyList()
if hasattr(gdb.Frame, 'select'):
    # Not all builds of gdb have gdb.Frame.select
    PyUp()
    PyDown()
PyBacktrace()
PyPrint()
PyLocals()