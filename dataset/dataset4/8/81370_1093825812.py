py = ctypes.PyDLL("", handle=sys.dllhandle)
missing = {name for name in EXPECTED_NAMES if not hasattr(py, name)}
# assert 'missing' is empty