
if os.name == 'win32':
    from msvcrt import setmode as _setmode
else:
    _setmode = None
