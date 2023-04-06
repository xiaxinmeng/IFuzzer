if not python3:
    from .exec_py2 import exec_
else:
    from .exec_py3 import exec_