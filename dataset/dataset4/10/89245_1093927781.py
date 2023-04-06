def c_buffer(init, size=None):
##    "deprecated, use create_string_buffer instead"
##    import warnings
##    warnings.warn("c_buffer is deprecated, use create_string_buffer instead",
##                  DeprecationWarning, stacklevel=2)
    return create_string_buffer(init, size)