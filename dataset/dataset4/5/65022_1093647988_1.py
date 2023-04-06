def pickle(ob_type, pickle_function, constructor_ob=None):
    if type(ob_type) is _ClassType:
        raise TypeError("copy_reg is not intended for use with classes")