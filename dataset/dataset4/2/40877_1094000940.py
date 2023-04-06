def packit(arg1, arg2, arg3, strng):
    return struct.pack(">LHH%ip"%len(strng), arg1, arg2,
arg3, strng)