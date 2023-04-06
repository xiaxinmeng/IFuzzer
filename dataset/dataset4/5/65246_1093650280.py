if convert_charrefs is _default_sentinel:
    convert_charrefs = False  # default
    warnings.warn("The value of convert_charrefs will become True in "
                  "3.5. You are encouraged to set the value explicitly.",
                  DeprecationWarning, stacklevel=2)